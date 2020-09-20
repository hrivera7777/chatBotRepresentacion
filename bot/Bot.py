from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response, get_most_frequent_response
#from chatterbot.comparisons import JaccardSimilarity
from similitud import JaccardSimilarity
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch

import os


def arranque():
    
    bot = ChatBot('Jaimito', #nombre del objeto
        response_selection_method=get_random_response,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                "statement_comparison_function": JaccardSimilarity,
                'maximum_similarity_threshold': 0.75,
                "response_selection_method": get_most_frequent_response,
                'default_response': 'solo se sobre estos pocos temas: ' + str(conocimientos()) + '. podrías formular diferente tu pregunta' 
            }
        ],
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.convert_to_ascii', # pre procesa la entrada quitando los acentos
            
        ],
        read_only=True)
    
    #"""
    trainer = ChatterBotCorpusTrainer(bot) # solo necesita entrenar una vez, por eso se mantienen comentadas las lineas

    trainer.train( 
        "./yml-entrena/"
    ) # cuando sea la primera vez que se usa, por favor descomentar estas lineas 
    #"""

    
    bot_input = bot.get_response('Hola')
    print('Jaimito > ' + str(bot_input))

    while True:
        try:
            entrada= input("Tú > ")
            lEntrada = entrada.lower() # se toma la entrada y se pone en minúsculas

            if(lEntrada in despedidaIn):
                print('Jaimito > Ok bye. :)')
                break

            bot_input = bot.get_response(lEntrada)
            print('Jaimito > ' + str(bot_input))

        except(KeyboardInterrupt, EOFError, SystemExit):
            break

#métodos adicional  solo para mejorar la visualización de lo que sabe el bot
def conocimientos():
    direc = os.fsencode("./yml-entrena/")
    lista=str(os.listdir(direc)).replace("b","").replace("'","").replace("[","").replace("]","").replace(".yml","")
    lista=list(lista.split(","))
    return lista

#list para cerrar el chat bot
despedidaIn=['chao', 'bye', 'hasta pronto','adios', 'hasta luego','nos vemos','que te vaya bien','gracias por todo']



arranque()



