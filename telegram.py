from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

app = FastAPI()


# https://oauth.telegram.org/auth?bot_id=547043436&origin=https%3A%2F%2Fcore.telegram.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcore.telegram.org%2Fwidgets%2Flogin
@app.get("/telegram/login")
async def telegram_login(request: Request):
    # Example URL
    telegram_auth_url = "https://oauth.telegram.org/auth"

    # Extract parameters from the provided URL
    bot_id = 547043436
    origin = "https://core.telegram.org"
    embed = 1
    request_access = "write"
    return_to = "https://core.telegram.org/widgets/login"

    print(bot_id, request_access, return_to, origin)
    if not bot_id or not origin or not return_to:
        raise HTTPException(status_code=400, detail="Missing required parameters")

    telegram_auth_params = {
        "bot_id": bot_id,
        "origin": origin,
        "embed": embed,
        "request_access": request_access,
        "return_to": return_to
    }
    telegram_auth_full_url = f"{telegram_auth_url}?{urlencode(telegram_auth_params)}"

    print(True)
    print(telegram_auth_full_url)
    return RedirectResponse(url=telegram_auth_full_url)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)