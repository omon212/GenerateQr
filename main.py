from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

class User(BaseModel):
    text_prompt: str
    qr_code_data: str

@app.post("/qr/")
async def generate_qr_code(user: User):
    payload = {
        "text_prompt": user.text_prompt,
        "qr_code_data": user.qr_code_data,
    }

    response = requests.post(
        "https://api.gooey.ai/v2/art-qr-code/",
        headers={
            "Authorization": "Bearer sk-Z6w1g92HyXNlGwzmis2PfXW3diSc0hXORusWzZkRhhPyzE8C",
            "Content-Type": "application/json",
        },
        json=payload
    )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    result = response.json()
    url = result['output']['output_images'][0]
    text_prompt = user.text_prompt

    return {"url": url, "text_prompt": text_prompt}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
