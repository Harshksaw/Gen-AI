from google import genai
from google.genai import types


client = genai.Client(api_key="")


response = client.chat.completions.create(
    model="gemini-1.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)