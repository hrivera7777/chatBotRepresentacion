import os

def conocimientos():
    direc = os.fsencode("./data/")
    lista=str(os.listdir(direc)).replace("b","").replace("'","").replace("[","").replace("]","").replace(".yml","")
    lista=list(lista.split(","))
    return lista

print(conocimientos())