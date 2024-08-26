
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
import chroma_cohere, chroma_chatgpt

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/chat/cohere/")
def chat_cohere(file_id: str, query: str):
    return chroma_cohere.generate_prompt(query, file_id)


@app.get("/chat/chatgpt/")
def chat_chatgpt(file_id: str, query: str):
    return chroma_chatgpt.generate_prompt(query, file_id)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)


