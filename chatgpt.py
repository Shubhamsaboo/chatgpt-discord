import openai

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_response(prompt):
    try:
        conversation_history = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"},
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].message.content.strip()
        return message
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't generate a response."