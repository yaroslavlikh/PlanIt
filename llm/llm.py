from llm.prompt import prompt_editing
from llm.gemini import client
from pydantic import BaseModel, Field
from typing import Literal

class Task(BaseModel):
    title: str = Field(min_length=1)
    start_date: str = Field(min_length=1)
    start_time: str = Field(default=" ")
    end_time: str = Field(default=" ")
    description: str = Field(default=" ")
    type_of: Literal["календарь", "задача"] = Field(default="задача")

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
