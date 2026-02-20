import json
import urllib.error
import urllib.request

from env import env

request_body = json.dumps({
    "model": "gpt-5-mini",
    "messages": [
        {
            "role": "user",
            "content": "What is the meaning of life?",
        },
    ],
}).encode()

req = urllib.request.Request(
    "https://codzen.ai/v1/chat/completions",
    data=request_body,
    headers={
        "Authorization": f"Bearer {env.CODZEN_TOKEN}",
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(json.dumps(data, indent=2))
except urllib.error.HTTPError as e:
    error_text = e.read().decode()
    msg = f"HTTP {e.code}: {error_text}"
    raise SystemExit(msg) from None
