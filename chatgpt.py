from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

async def generate_response(prompt):
    try:
        conversation_history = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"},
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history,
            max_tokens=350,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].message.content.strip()
        return message
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't generate a response."
