from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

from main import predict_vid

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.post("/reading_test")
async def reading(info : Request):
    req_info = await info.json()
    try:
        link =dict(req_info)["link"] 
        print(dict(req_info)["link"])
        return {"message": "success", "link_recived":link}
    except Exception as e:
        print(e)
        return {"message": "link not found"}



