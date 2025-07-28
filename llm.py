from huggingface_hub import InferenceClient
import os

# Model and token
MODEL_ID = "Qwen/Qwen3-Coder-480B-A35B-Instruct"
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize client
client = InferenceClient(token=HF_TOKEN)

def generate_sql(prompt):
    system_prompt = (
        "You are a helpful assistant that converts plain English into syntactically correct MySQL SQL queries. "
        "Only return SQL code without any explanation or extra text."
    )

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=256,
    )

    return response.choices[0].message.content.strip()
