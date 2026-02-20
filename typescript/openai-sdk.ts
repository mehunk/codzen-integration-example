import OpenAI from '@openai/openai';

import { env } from './env';

const openai = new OpenAI({
  baseURL: `${env.API_BASE_URL}/v1`,
  apiKey: env.CODZEN_TOKEN,
});

const completion = await openai.chat.completions.create({
  model: env.MODEL,
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life?',
    },
  ],
});

console.log('Response:', completion.choices[0]?.message.content);
