import { env } from './env';

const response = await fetch(`${env.API_BASE_URL}/v1/chat/completions`, {
  method: 'POST',
  headers: {
    Authorization: `Bearer ${env.CODZEN_TOKEN}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: env.MODEL,
    messages: [
      {
        role: 'user',
        content: 'What is the meaning of life?',
      },
    ],
  }),
});

if (!response.ok) {
  const errorText = await response.text();
  throw new Error(`HTTP ${response.status}: ${errorText}`);
}

const data = await response.json();
console.log(JSON.stringify(data, null, 2));
