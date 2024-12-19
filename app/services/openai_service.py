import openai
from app.config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_text_with_ai(text: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Vous êtes un assistant."},
                {"role": "user", "content": f"{text}"}
            ],
            max_tokens=100

        )

        #return response["choices"][0]["message"]["content"].strip()
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Erreur lors de l'appel à l'API OpenAI : {e}")
