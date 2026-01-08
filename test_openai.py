from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in one sentence"}]
)

print(res.choices[0].message.content)
