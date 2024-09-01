const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

export default async function Home() {
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${OPENAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'gpt-4o', // Replace with the model you want to use
      messages: [{ role: 'user', content: 'some sample prompt' }],
      max_tokens: 100, // Set token limit
      temperature: 0.7, // Set the temperature
    }),
  });

  const data = await response.json();
  console.log(data.choices);
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      {data.choices[0].message.content}
    </main>
  );
}
