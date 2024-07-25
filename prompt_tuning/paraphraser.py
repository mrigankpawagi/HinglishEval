import http.client
import os
from dotenv import load_dotenv
import json

def paraphrase(text: str) -> str:
    load_dotenv()
    api_key = os.getenv("RAPID_API_KEY")

    conn = http.client.HTTPSConnection("paraphrase-genius.p.rapidapi.com")

    # Prepare the payload dynamically
    payload = json.dumps({
        "text": text,
        "result_type": "multiple"
    })

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "paraphrase-genius.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    conn.request("POST", "/dev/paraphrase/", payload, headers)

    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
