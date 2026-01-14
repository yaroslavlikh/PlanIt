
from llm.prompt import prompt_editing
from llm.gemini import client
def ask_qwen(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents=prompt_editing + prompt,
        generation_config={
            "response_mime_type": "application/json"
        }
    )
    print(f'результат: {response.text}')
    return response.text