const { OpenAI } = require('openai');
const openai = new OpenAI(process.env.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);

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const prompt = req.body.prompt;
    const completions = await openai.complete({
      engine: 'davinci-5x',
      prompt,
      maxTokens: 150,
      n: 1,
      stop: ['\n'],
    });
    const message = completions.choices[0].text.trim();
    res.status(200).json({ message });
  } else {
    res.status(405).send('Method not allowed');
  }
}
