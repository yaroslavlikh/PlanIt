
from llm.prompt import prompt_editing
from llm.gemini import client
def ask_qwen(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest", contents=prompt_editing + prompt
    )
    print(f'результат: {response.text}')
    return response.text