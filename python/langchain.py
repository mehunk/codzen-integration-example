from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from env import env

# Create ChatOpenAI model with custom configuration
model = ChatOpenAI(
    base_url="https://codzen.ai/v1",
    api_key=SecretStr(env.CODZEN_TOKEN),
    model="gpt-5-mini",
)

# Invoke the model with a human message
response = model.invoke([HumanMessage(content="What is the meaning of life?")])

print("Response:", response.content)  # type: ignore[reportUnknownArgumentType]
