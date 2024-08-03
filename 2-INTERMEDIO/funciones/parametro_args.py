#forma optima de sumar valores con el parametro args
def suma (*numeros):#si lo usamos no podemos poner otros parametros despues, antes si 
    return sum(numeros)

resultado = suma(5,3,1,89,18,1,64,44,498)

def suma_total (numeros):#si lo usamos no podemos poner otros parametros despues, antes si 
    return sum([*numeros])

resultado2 = suma_total(5,3,1,89,18,1,64,44,498)