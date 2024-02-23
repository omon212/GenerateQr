import requests

# Define the payload for the request
payload = {
    "text_prompt": "Hello, ahmad kot",
    "output": {
        'shortened_url': "https://omonullo.uz/"
    }
}


payload['output']['shortened_url'] = 'omon'

response = requests.post(
    "https://api.gooey.ai/v2/art-qr-code/",

    headers={
        "Authorization": "Bearer " + "sk-2J4ocYtNQ3tXzUOjXSYMuJciW0VE8977xacZB6WS3lbVkTl8",
    },
    json=payload,
)

if response.status_code == 200:
    response_json = response.json()
    if 'output' in response_json:
        if 'shortened_url' in response_json['output']:
            response_json['output']['shortened_url'] = 'https://omonullo.uz/'
            print(response_json)
else:
    print("Error:", response.status_code, response.text)