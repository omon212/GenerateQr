from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/api/{value}")
def salom_dunyo(value: str):
    payload = {
        "text_prompt": "Create Beautiful Qr code WebSite",
        "qr_code_data": f"{value}",
    }

    response = requests.post(
        "https://api.gooey.ai/v2/art-qr-code/",
        headers={
            "Authorization": "Bearer " + "sk-Z6w1g92HyXNlGwzmis2PfXW3diSc0hXORusWzZkRhhPyzE8C",
        },
        json=payload
    )

    url = response.json()['url']
    print(response.json())
    return url