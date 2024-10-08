import openai
import dotenv
import os

dotenv.load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

messages = [
  {
    "role":"system",
    "content":"あなたは端的に発言するAIです。"
  },
  {
    "role":"user",
    "content":"こんにちは"
  }
]

res = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  message=messages,
)
print(res["choices"][0]["message"]["content"])