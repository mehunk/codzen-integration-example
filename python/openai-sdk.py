from openai import OpenAI

from env import env

# Create OpenAI client with custom base URL, API key, and SSL context
openai = OpenAI(base_url="https://codzen.ai/v1", api_key=env.CODZEN_TOKEN)

# Create chat completion
completion = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role": "user",
            "content": "What is the meaning of life?",
        },
    ],
)

# Print the response content
print("Response:", completion.choices[0].message.content)
