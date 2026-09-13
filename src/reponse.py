
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
from groq import Groq
client = Groq(api_key=api_key)


def reponse(prompt,client,model_reponse):

    """
    Cette fonction prend comme paramètre le prompt et le client. Le client désigne l'objet reçu après 
    avoir fait appel à notre clé API. model_reponse désigne le modèle de LLM qu'on utilisera avec notre clé
    API pour utiliser le contexte et répondre.

    """

    response = client.chat.completions.create(model=model_reponse,
                                          messages= prompt)

    return (response.choices[0].message.content)
