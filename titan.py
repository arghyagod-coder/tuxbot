import requests
import json

def shorten(url:str, alias_type:str = 'random', alias: str = "") -> str:
    endpoint = f"http://titan-url.herokuapp.com/shorten"
    url = url.replace("<", "").replace(">", "")

    payload = {
        "original-url": url,
        "alias-type": alias_type,
        "slug": alias
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "binod-discord-bot"
    }

    r = requests.post(endpoint, headers = headers, json = payload)
    data = json.loads(r.text)

    if not data["ok"]:
        message = data["message"]
        return f"Unable to shorten the URL `<{url}>`. \nError: {message}"

    return "Here's your shortened URL: <{}>".format(data["message"])