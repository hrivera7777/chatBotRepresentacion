from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot("nombre")
trainer = ChatterBotCorpusTrainer(chat) 
trainer.train("chatterbot.corpus.spanish")

while True:
    peticion = input('You:')
    respuesta = chat.get_response(peticion)
    print('Bot: ', respuesta)
