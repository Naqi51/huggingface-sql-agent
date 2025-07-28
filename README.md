
````markdown
# 🤖 AI DBA Agent – Natural Language to MySQL

AI DBA Agent is a local assistant that converts plain English instructions into valid MySQL queries and executes them on a connected MySQL database.

> “Create a table named employees with columns id, name, and salary”  
> → ✅ `CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(100), salary FLOAT);`

---

## 🚀 Features

- ✅ Natural language to SQL using LLM (Hugging Face Qwen3-Coder)
- ✅ Executes SQL directly on your MySQL instance
- ✅ Supports:
  - Creating/Dropping databases & tables
  - Inserting, updating, deleting records
  - Viewing, joining, filtering, and counting data
- ✅ Persistent `USE database` context
- ✅ Logs all executed queries (`query_log.txt`)


---

## 🛠️ Tech Stack

- Python 3.10+
- Hugging Face Inference API
- MySQL (local or remote)
- LLM: `Qwen/Qwen3-Coder-480B-A35B-Instruct`

---


````

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Set your Hugging Face API token

```bash
export HF_TOKEN=your_hf_token_here
```

> 🔐 You can also use `.env` file + `python-dotenv` if preferred.

### 4. Update MySQL connection

Edit `db.py` and set your MySQL credentials:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)
```

---

## ▶️ Run the Agent

```bash
python3 main.py
```

---

## 💬 Example Prompts

```text
Create a database named employee_db
Use employee_db
Create table employees with id int primary key, name varchar(100)
Insert into employees values (1, 'Alice')
Show all records from employees
Drop the table employees
```

---

## 📁 Project Structure

```
ai-dba-agent/
├── main.py             # Command-line interface
├── llm.py              # Hugging Face SQL generation
├── db.py               # SQL executor with DB selection
├── requirements.txt    # Python dependencies
└── query_log.txt       # Auto-generated query history
```

---

## 📜 License

MIT License © 2025 \[Your Name]

---

## 🙋‍♂️ Author

* **Mohammad Naqiuddin**
* GitHub: [@Naqi51](https://github.com/Naqi51)
* Built with ❤️ using MySQL + LLM

