import httpx
from openai import OpenAI

from env import env

# Create OpenAI client with custom base URL, API key, and SSL context
openai = OpenAI(
    base_url=f"{env.API_BASE_URL}/v1",
    api_key=env.CODZEN_TOKEN,
    http_client=httpx.Client(verify=False),  # noqa: S501
)

# Create chat completion
completion = openai.chat.completions.create(
    model=env.MODEL,
    messages=[
        {
            "role": "user",
            "content": "What is the meaning of life?",
        },
    ],
)

# Print the response content
print("Response:", completion.choices[0].message.content)
