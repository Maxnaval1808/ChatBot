from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("en_core_web_sm")
# Esse modelo é preciso para o ChatterBot funcionar corretamente

chatbot = ChatBot("BotTw")
# Create a chatbot instance with the specified language model

sentenca = [
    "Opa",
    "Como vai?",
    "Qual é o seu nome?",
    "Sou o BotTw e vou te ajudar na carreira de tecnologia",
    "Qual formação você indica em Python?",
    "Recomendo a formação Flask",
    "Qual tecnologia está em alta no momento?",
    "A tecnologia Flutter"
]

treino = ListTrainer(chatbot)
treino.train(sentenca)

while True:
    mensagem = input("Envie uma mensagem:\n")
    if mensagem.lower() == "sair":
        break

    resposta = chatbot.get_response(mensagem)
    if float(resposta.confidence) > 0.4:
        print("BotTw: ", resposta)
    else:
        print("BotTw: Desculpe, ainda não sei responder esta pergunta")