import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://openrouter.ai/api/v1"

response = openai.ChatCompletion.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Respond in German"},
        {"role": "user", "content": "Say 'Hello world'"}
    ],
    temperature=0.7,
    max_tokens=150,
)

response_message = response["choices"][0]["message"]
print(response_message)
