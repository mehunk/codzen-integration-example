import httpx
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from env import env

# Create ChatOpenAI model with custom configuration
model = ChatOpenAI(
    base_url=f"{env.API_BASE_URL}/v1",
    api_key=SecretStr(env.CODZEN_TOKEN),
    model=env.MODEL,
    http_client=httpx.Client(verify=False),  # noqa: S501
)

# Invoke the model with a human message
response = model.invoke([HumanMessage(content="What is the meaning of life?")])

print("Response:", response.content)  # type: ignore[reportUnknownArgumentType]
