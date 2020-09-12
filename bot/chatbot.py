from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response, get_most_frequent_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch

import os

def temas():
    directory = os.fsencode("./data/")
    lista=str(os.listdir(directory)).replace("b","").replace("'","").replace("[","").replace("]","").replace(".yml","")
    lista=list(lista.split(","))
    return lista

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
def run(inicial):

    bot = ChatBot('Norman',
        response_selection_method=get_random_response,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                "statement_comparison_function": levenshtein_distance,
                'maximum_similarity_threshold': 0.90,
                'default_response': "Perdon solo se sobre :"+str(temas()) #'Disculpa, no te he entendido bien, mi único conocimiento es acerca de Representación del Conocimiento. ¿Puedes ser más específico?.'
            }
        ],
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.convert_to_ascii',
        ],
        read_only=True)

    trainer = ChatterBotCorpusTrainer(bot)



    trainer.train(
        "./data/"
        #"./data/basicES.yml",
        #"./data/knwl-representation.yml",
        #"./data/production-rules.yml",
    #"./data/semantic-networks.yml",
        ##"./data/logicaPredicados.yml",
        #"./data/frames.yml"
    )

    entrada2= "Es la frase que no supo interpretar"
    if(inicial != ""):
        bot_input = bot.get_response(inicial)
        print(bot_input)
    while True:
        try:
            entrada= input()
            if (entrada =='**'):
                agregar(entrada2)
                run(entrada2)
                exit()
            else:
                entrada2 = entrada   
            bot_input = bot.get_response(entrada)
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break



run("")