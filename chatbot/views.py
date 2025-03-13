import openai
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

# On utilise la clé OpenAI stockée dans settings.py
openai.api_key = settings.OPENAI_API_KEY

@api_view(["POST"])
def chatbot(request):
    user_input = request.data.get("message")  # Récupère le message de l'utilisateur

    # Envoi du message à l'API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Ou "gpt-3.5-turbo" si tu veux un modèle plus rapide
        messages=[
            {"role": "system", "content": "Tu es un assistant médical. Pose des questions pour affiner le diagnostic."},
            {"role": "user", "content": user_input}
        ]
    )

    # Retourne la réponse du chatbot
    return Response({"response": response["choices"][0]["message"]["content"]})
