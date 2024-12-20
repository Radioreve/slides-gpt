import openai

from app.config import Config

openai.api_key = Config.OPENAI_API_KEY


def generate_text_with_ai(text: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": text}
            ],
            max_tokens=Config.MAX_TOKEN
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Erreur lors de l'appel à l'API OpenAI : {e}")
