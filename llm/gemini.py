from google import genai
from config import get_token_gemini

token = get_token_gemini()
client = genai.Client(api_key=token)