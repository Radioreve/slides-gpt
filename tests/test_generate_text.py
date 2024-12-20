import unittest
from unittest import mock
from openai.types import CompletionUsage
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice
from openai.types.completion_usage import CompletionTokensDetails, PromptTokensDetails
from app.services.openai_service import generate_text_with_ai

class TestOpenAIService(unittest.TestCase):

    def test_generate_text_with_ai_exception(self):
        text = (
            """
            FastAPI est un framework web moderne et rapide (haute performance) pour la création d'API avec Python, basé sur les annotations de type standard de Python.
            Les principales fonctionnalités sont :
            Rapidité : De très hautes performances, au niveau de NodeJS et Go (grâce à Starlette et Pydantic). L'un des frameworks Python les plus rapides.
            Rapide à coder : Augmente la vitesse de développement des fonctionnalités d'environ 200 % à 300 %. *
            Moins de bugs : Réduit d'environ 40 % les erreurs induites par le développeur. *
            Intuitif : Excellente compatibilité avec les IDE. Complétion complète. Moins de temps passé à déboguer.
            Facile : Conçu pour être facile à utiliser et à apprendre. Moins de temps passé à lire la documentation.
            Concis : Diminue la duplication de code. De nombreuses fonctionnalités liées à la déclaration de chaque paramètre. Moins de bugs.
            Robuste : Obtenez un code prêt pour la production. Avec une documentation interactive automatique.
            Basé sur des normes : Basé sur (et entièrement compatible avec) les standards ouverts pour les APIs : OpenAPI (précédemment connu sous le nom de Swagger) et JSON Schema
            """
        )

        with mock.patch("openai.chat.completions.create") as mock_create:
            mock_create.side_effect = Exception("Error code: 429 - You exceeded your current quota.")
            with self.assertRaises(Exception) as exc_info:
                generate_text_with_ai(text)

            self.assertIn("Error code: 429 - You exceeded your current quota.", str(exc_info.exception))

    def test_generate_text_with_ai_success(self):
        text = (
            """
            FastAPI est un framework web moderne et rapide (haute performance) pour la création d'API avec Python, basé sur les annotations de type standard de Python.
            Les principales fonctionnalités sont :
            Rapidité : De très hautes performances, au niveau de NodeJS et Go (grâce à Starlette et Pydantic). L'un des frameworks Python les plus rapides.
            Rapide à coder : Augmente la vitesse de développement des fonctionnalités d'environ 200 % à 300 %. *
            Moins de bugs : Réduit d'environ 40 % les erreurs induites par le développeur. *
            Intuitif : Excellente compatibilité avec les IDE. Complétion complète. Moins de temps passé à déboguer.
            Facile : Conçu pour être facile à utiliser et à apprendre. Moins de temps passé à lire la documentation.
            Concis : Diminue la duplication de code. De nombreuses fonctionnalités liées à la déclaration de chaque paramètre. Moins de bugs.
            Robuste : Obtenez un code prêt pour la production. Avec une documentation interactive automatique.
            Basé sur des normes : Basé sur (et entièrement compatible avec) les standards ouverts pour les APIs : OpenAPI (précédemment connu sous le nom de Swagger) et JSON Schema
            """
        )

        simulated_response = ChatCompletion(
            id='chatcmpl-AfrFgIlCLfbV54WpbayzS3i5y7S4S',
            choices=[Choice(
                finish_reason='stop',
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content='FastAPI est un framework web rapide basé sur les annotations de type de Python pour créer des API.',
                    refusal=None,
                    role='assistant',
                    audio=None,
                    function_call=None,
                    tool_calls=None
                )
            )],
            created=1734539512,
            model='gpt-3.5-turbo-0125',
            object='chat.completion',
            service_tier=None,
            system_fingerprint=None,
            usage=CompletionUsage(
                completion_tokens=21,
                prompt_tokens=67,
                total_tokens=88,
                completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0),
                prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))

        with mock.patch("openai.chat.completions.create", return_value=simulated_response) as mock_create:
            result = generate_text_with_ai(text)
            self.assertEqual(result, "FastAPI est un framework web rapide basé sur les annotations de type de Python pour créer des API.")

if __name__ == '__main__':
    unittest.main()
