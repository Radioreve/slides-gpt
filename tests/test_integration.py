import unittest
from app.services.openai_service import generate_text_with_ai

class TestGenerateText(unittest.TestCase):

    def test_generate_text(self):
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
            Basé sur des normes : Basé sur (et entièrement compatible avec) les standards ouverts pour les APIs : OpenAPI (précédemment connu sous le nom de Swagger) et JSON Schema.
            """
        )

        result = generate_text_with_ai(f"Résumé du texte suivant : {text}")

        self.assertIsInstance(result, str, "Le résultat doit être une chaîne de caractères")
        self.assertGreater(len(result), 0, "Le résumé ne doit pas être vide")

if __name__ == '__main__':
    unittest.main()
