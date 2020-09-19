from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response, get_most_frequent_response
from chatterbot.comparisons import levenshtein_distance
#from chatterbot.comparisons import JaccardSimilarity
from similitud import JaccardSimilarity
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch

import os

jaccard_similarity = JaccardSimilarity()

"""
"""
"""
def agregar(pregunta):
    print("la pregunta "+pregunta+" a que tema pertenece?")
    i=1
    print("[0]    Otro")
    TEM=temas()
    for tema in TEM:
        print ("[{}]    {}".format(i,tema))
        i+=1
    selec =int(input())
    if (selec==0):
        direc='./data/' + input("nombre del archivo a guardar") + '.yml'
        with open(direc,'w') as f:
            f.write("- - \""+ pregunta+"\"\n")
            f.write("  - "+input("cual es la respuesta a:"+pregunta+"? ")+"\n")
        return 
            
    if (selec>len(TEM)):
        print("si no es ninguno de los temas escoja 0")
        agregar(pregunta)
        return 

    else:
        direc='./data/'+TEM[selec-1]+'.yml'
        with open(direc,'a') as f:
            f.write("- - \""+ pregunta+"\"\n")
            f.write("  - "+input("cual es la respuesta a:"+pregunta+"? ")+"\n")
        return 
"""

def arranque():
    
    bot = ChatBot('Jaimito', #nombre del objeto
        response_selection_method=get_random_response,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                #"statement_comparison_function": levenshtein_distance,
                "statement_comparison_function": JaccardSimilarity,
                'maximum_similarity_threshold': 0.75,
                "response_selection_method": get_most_frequent_response,
                'default_response': 'solo se sobre estos pocos temas: ' + str(conocimientos()) + '. podrías formular diferente tu pregunta' #Lo siento podrías formular diferente tu pregunta' 
            }
        ],
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.convert_to_ascii', # pre procesa la entrada quitando los acentos
            
        ],
        read_only=True)
    """
    trainer = ChatterBotCorpusTrainer(bot) # solo necesita entrenar una vez, por eso se mantienen comentadas las lineas

    trainer.train( 
        "./yml-entrena/"
    ) # cuando sea la primera vez que se usa, por favor descomentar estas lineas 
    """


    #entrada2= "Es la frase que no supo interpretar"
    #if(inicial != ""):
    """
    bot_input = bot.get_response(inicio) #entraba desde el metodo
    print('Jaimito >' + str(bot_input))
    """
    print('Jaimito > ¡Hola!')
    while True:
        try:
            entrada= input("Tú > ")
            lEntrada = entrada.lower() # se toma la entrada y se pone en minúsculas
            """
            if (entrada =='**'):
                agregar(entrada2)
                run(entrada2)
                exit()
            else:
                entrada2 = entrada   
            """
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

#print(str(jaccard_similarity.get_stopwords()))

arranque()



