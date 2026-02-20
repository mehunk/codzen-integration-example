#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load environment variables from .env file
if [[ -f "$SCRIPT_DIR/.env" ]]; then
  set -a
  source "$SCRIPT_DIR/.env"
  set +a
fi

response=$(curl -s -w "\n%{http_code}" "${API_BASE_URL}/v1/chat/completions" \
  -X POST \
  -H "Authorization: Bearer ${CODZEN_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"${MODEL}"'",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  }')

http_code="${response##*$'\n'}"
body="${response%$'\n'*}"

if [[ "$http_code" -lt 200 || "$http_code" -ge 300 ]]; then
  echo "HTTP ${http_code}: ${body}" >&2
  exit 1
fi

echo "${body}"
