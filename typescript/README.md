# Codzen Integration Example — TypeScript

This project demonstrates three ways to integrate with the [Codzen](https://codzen.ai) API using TypeScript and Bun. All examples use the OpenAI-compatible chat completions endpoint.

## Integration Approaches

| File | Approach | Description |
|---|---|---|
| [fetch-api.ts](fetch-api.ts) | Raw Fetch API | Direct HTTP POST with no SDK dependencies |
| [openai-sdk.ts](openai-sdk.ts) | OpenAI SDK | Official `@openai/openai` SDK pointed at Codzen's endpoint |
| [langchain.ts](langchain.ts) | LangChain | `ChatOpenAI` from `@langchain/openai` for framework-level integration |

## Prerequisites

- [Bun](https://bun.com) runtime
- A Codzen API token

## Setup

Install dependencies:

```bash
bun install
```

Create a `.env` file in this directory with the following variables:

```env
CODZEN_TOKEN=your_api_token_here
MODEL=your_model_id_here
API_BASE_URL=https://your.codzen.endpoint
```

## Running the Examples

```bash
# Raw Fetch API
bun run fetch-api

# OpenAI SDK
bun run openai-sdk

# LangChain
bun run langchain
```

## Project Structure

```
.
├── env.ts          # Type-safe environment variable validation (Zod + @t3-oss/env-core)
├── fetch-api.ts    # Integration via native Fetch API
├── openai-sdk.ts   # Integration via OpenAI TypeScript SDK
├── langchain.ts    # Integration via LangChain framework
├── package.json
├── tsconfig.json
└── biome.json      # Linting and formatting config
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `CODZEN_TOKEN` | Yes | Bearer token for API authentication |
| `MODEL` | Yes | Model identifier to use for completions |
| `API_BASE_URL` | Yes | Base URL of the Codzen API endpoint |

## Tech Stack

- **Runtime:** Bun
- **Language:** TypeScript
- **Linting/Formatting:** Biome
- **Schema Validation:** Zod + @t3-oss/env-core
- **AI SDKs:** `@openai/openai`, `@langchain/openai`, `@langchain/core`
