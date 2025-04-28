from fastapi import FastAPI 
from ollama import Client

app= FastAPI()

client= Client(
    host="http://localhost:11434",
    
)

client.pull("gemma3:1b")
@app.get("/chat")
def chat(message: str = Body(..., description="Chat Message")):
    response = client.chat(model ="gemma3:1b", messages=[
        {"role": "user", "content": "Hello, how are you?"},
    ])
    return response["message"]["content"]   
