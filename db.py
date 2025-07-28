import mysql.connector
from datetime import datetime

connection = None
selected_db = None

def connect():
    global connection
    if connection is None or not connection.is_connected():
        connection = mysql.connector.connect(
            host="192.168.1.29",  # your MySQL host
            user="dba",
            password="dba",
        )

def log_query(query, result):
    with open("query_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] QUERY:\n{query.strip()}\n")
        f.write(f"RESULT:\n{str(result)}\n\n")

def execute_sql(query):
    global connection, selected_db
    connect()
    cursor = connection.cursor()

    # Handle USE <db>
    if query.strip().lower().startswith("use "):
        selected_db = query.strip().split()[1].strip(";")
        connection.database = selected_db
        cursor.execute(query)
        log_query(query, f"✅ Switched to database: {selected_db}")
        return f"✅ Switched to database: {selected_db}"

    if selected_db:
        connection.database = selected_db

    try:
        cursor.execute(query)

        # For SELECT/SHOW
        if query.strip().lower().startswith(("select", "show")):
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            result = "\n".join([" | ".join(columns)] + [" | ".join(map(str, row)) for row in rows])
            log_query(query, result)
            return result

        connection.commit()
        log_query(query, "✅ Query executed successfully.")
        return "✅ Query executed successfully."

    except mysql.connector.Error as err:
        log_query(query, f"❌ Error: {err}")
        return f"❌ Error: {err}"

    finally:
        cursor.close()
