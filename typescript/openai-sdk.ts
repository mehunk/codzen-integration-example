import OpenAI from '@openai/openai';

import { env } from './env';

const openai = new OpenAI({
  baseURL: 'https://codzen.ai/v1',
  apiKey: env.CODZEN_TOKEN,
});

const completion = await openai.chat.completions.create({
  model: 'gpt-5-mini',
  messages: [
    {
      role: 'user',
      content: 'What is the meaning of life?',
    },
  ],
});

console.log('Response:', completion.choices[0]?.message.content);
