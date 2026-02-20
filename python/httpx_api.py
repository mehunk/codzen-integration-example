import json

import httpx

from env import env

try:
    response = httpx.post(
        "https://codzen.ai/v1/chat/completions",
        json={
            "model": "gpt-5-mini",
            "messages": [
                {
                    "role": "user",
                    "content": "What is the meaning of life?",
                },
            ],
        },
        headers={
            "Authorization": f"Bearer {env.CODZEN_TOKEN}",
            "Content-Type": "application/json",
        },
        timeout=30.0,
    )
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=2))
except httpx.HTTPStatusError as e:
    msg = f"HTTP {e.response.status_code}: {e.response.text}"
    raise SystemExit(msg) from None
