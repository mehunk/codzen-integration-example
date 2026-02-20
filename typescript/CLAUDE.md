## Project Overview

This is a TypeScript example project showing three ways to integrate with the Codzen API (OpenAI-compatible):

- **[fetch-api.ts](fetch-api.ts)** — Raw Fetch API, no SDK
- **[openai-sdk.ts](openai-sdk.ts)** — Official `@openai/openai` SDK
- **[langchain.ts](langchain.ts)** — LangChain `ChatOpenAI` wrapper

Environment variables are validated at startup via `env.ts` using Zod + `@t3-oss/env-core`. Required vars: `CODZEN_TOKEN`, `MODEL`, `API_BASE_URL`.

Run any example with `bun run <script-name>` (scripts defined in `package.json`).

---

Default to using Bun instead of Node.js.

- Use `bun <file>` instead of `node <file>` or `ts-node <file>`
- Use `bun test` instead of `jest` or `vitest`
- Use `bun build <file.html|file.ts|file.css>` instead of `webpack` or `esbuild`
- Use `bun install` instead of `npm install` or `yarn install` or `pnpm install`
- Use `bun run <script>` instead of `npm run <script>` or `yarn run <script>` or `pnpm run <script>`
- Use `bunx <package> <command>` instead of `npx <package> <command>`
- Bun automatically loads .env, so don't use dotenv.

## APIs

- `Bun.serve()` supports WebSockets, HTTPS, and routes. Don't use `express`.
- `bun:sqlite` for SQLite. Don't use `better-sqlite3`.
- `Bun.redis` for Redis. Don't use `ioredis`.
- `Bun.sql` for Postgres. Don't use `pg` or `postgres.js`.
- `WebSocket` is built-in. Don't use `ws`.
- Prefer `Bun.file` over `node:fs`'s readFile/writeFile
- Bun.$`ls` instead of execa.

## Testing

Use `bun test` to run tests.

```ts#index.test.ts
import { test, expect } from "bun:test";

test("hello world", () => {
  expect(1).toBe(1);
});
```


