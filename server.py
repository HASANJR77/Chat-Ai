from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import uvicorn

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(data: ChatMessage):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "Senin adın Chat-AI. Her zaman Türkçe konuşan yardımsever bir yapay zekâsın."
                },
                {
                    "role": "user",
                    "content": data.message
                }
            ]
        )

        return {
            "reply": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "reply": str(e)
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)