# Codzen Integration Example — Python

This project demonstrates how to integrate with the [Codzen](https://codzen.ai) API using Python. All examples use the OpenAI-compatible chat completions endpoint.

## Integration Approaches

| File | Approach | Description |
|---|---|---|
| [fetch_api.py](fetch_api.py) | urllib (stdlib) | Direct HTTP POST with no third-party HTTP dependencies |
| [openai-sdk.py](openai-sdk.py) | OpenAI SDK | Official OpenAI Python client with custom base URL |
| [langchain.py](langchain.py) | LangChain | LangChain's `ChatOpenAI` wrapper for chat completions |

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager
- A Codzen API token

## Setup

Install dependencies:

```bash
uv sync
```

Create a `.env` file in this directory with the following variables:

```env
CODZEN_TOKEN=your_api_token_here
MODEL=your_model_id_here
API_BASE_URL=https://codzen.ai
```

## Running the Examples

```bash
uv run python fetch_api.py
uv run python openai-sdk.py
uv run python langchain.py
```

## Project Structure

```
.
├── env.py          # Type-safe environment variable validation (pydantic-settings)
├── fetch_api.py    # Integration via urllib (standard library)
├── openai-sdk.py   # Integration via OpenAI Python SDK
├── langchain.py    # Integration via LangChain
├── pyproject.toml
└── README.md
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `CODZEN_TOKEN` | Yes | Bearer token for API authentication |
| `MODEL` | Yes | Model identifier to use for completions |
| `API_BASE_URL` | Yes | Base URL of the Codzen API endpoint (must be a valid URL) |

## Tech Stack

- **Runtime:** Python 3.14
- **Package Manager:** uv
- **Linting/Formatting:** Ruff
- **Type Checking:** Pyright (Pylance)
- **Env Validation:** pydantic-settings
