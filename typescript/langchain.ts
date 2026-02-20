import { HumanMessage } from '@langchain/core/messages';
import { ChatOpenAI } from '@langchain/openai';

import { env } from './env';

const model = new ChatOpenAI({
  configuration: {
    baseURL: `${env.API_BASE_URL}/v1`,
    apiKey: env.CODZEN_TOKEN,
  },
  model: env.MODEL,
});

const response = await model.invoke([
  new HumanMessage('What is the meaning of life?'),
]);

console.log('Response:', response.content);
