from fastapi import FastAPI
import os
import requests
from starlette.responses import HTMLResponse

# Create an instance of the FastAPI class
app = FastAPI()


# Define a route using a decorator with a path parameter
@app.get("/api/{value}")
def salom_dunyo(value: str):
    payload = {
        "text_prompt": value
    }

    response = requests.post(
        "https://api.gooey.ai/v2/art-qr-code/",
        headers={
            "Authorization": "Bearer " + "sk-9lRYItqASSR0CXluaKAqdVi4TVGk4ufLCWYk3Ah0wNms7AbR",
        },
        json=payload,
    )
    assert response.ok, response.content

    result = response.json()
    print(result)
    shortened_images = result['output']['output_images']
    if shortened_images:
        url = shortened_images[0]
    else:
        url = ""


    # haqiqiy_url = url['output']['output_images']
    # print(haqiqiy_url)
    html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>QR Code Display</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f0f0f0;
                    }}
                    img {{
                        max-width: 80%;
                        max-height: 80%;
                    }}
                </style>
            </head>
            <body>
                <img src="{url}" alt="QR Code">
            </body>
            </html>
    """

    return HTMLResponse(content=html_content)

