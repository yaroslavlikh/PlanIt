import requests
from api.prompt import prompt_editing

def ask_qwen(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt_editing + prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,   # меньше = точнее
                "num_ctx": 2048       # макс. длина контекста
            }
        }
    )
    print(response.json()['response'])
    return response.json()['response']