import requests

def ask_qwen(prompt):
    prompt_editing = "Верни заданные дальше данные в формате '{Название меро (обязательно придумай)}, " \
    "{дата и время начала (пиши в датах типа 23 ноября и тд)), если прямо сказано, иначе пробел}, " \
    "{дата и время конца, если прямо сказано, иначе пробел}, {описание, если есть, иначе пробел}': "
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5",
            "prompt": prompt_editing + prompt,
            "stream": False
        }
    )
    print(response.json()['response'])
    return response.json()['response']