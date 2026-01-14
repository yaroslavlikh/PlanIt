from llm.prompt import prompt_editing
from llm.gemini import client
from pydantic import BaseModel, Field

class TypeOfTask(BaseModel):
    calendar = "календарь"
    task = "задача"

class Task(BaseModel):
    title: str = Field(min_length=1)
    start_date: str = Field(min_length=1)
    start_time: str = Field(min_length=4)
    end_time: str = Field(default=" ")
    description: str = Field(default=" ")
    type_of: TypeOfTask = Field(default="задача")

def ask_qwen(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents=prompt_editing + prompt,
        config={
        "response_mime_type": "application/json",
        "response_json_schema": Task.model_json_schema()
        }
    )
    res = Task.model_validate_json(response.text)
    print(f'результат: {res}')
    return res
