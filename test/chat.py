#chat bot para sistemas inteligentes sobre representación del conocimiento
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot(
    "Chat Bot 1.0",
    trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
)

chatBot.train(
    "chatterbot.corpus.spanish"

)
