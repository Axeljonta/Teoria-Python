#formas de crea conjuntos 

#crando tupla con set()
conjunto = set(['dato1','dato2']) #no se puede poner una lista dentro de un conjunto tampoco otro conjunto, una tupla si

conjuntoA =  {'dato1',  'dato2'}

#metiendo conjuntos dentro de otros conjuntos
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1, 'dato3'}

#TEORIA DE CONJUNTOS
#Si tengo el conjunto A y un conjunto B que incluye a A dentro, el conjunto A seria un subconjunto y B seria un conjunto o A seria un conjunto y B un superconjunto 
conjunto3 = {1,32,5,45}
conjunto4 = {1,5}
conjunto5 = {2,31}

#verificando si es un subconjunto 
resultado = conjunto4.issubset(conjunto3)
resultado1 = conjunto4 <= conjunto3 
print(resultado, resultado1)

#verificando si es un superconjunto 
resultado = conjunto3.issuperset(conjunto4)
resultado1 = conjunto3 > conjunto4 
print(resultado, resultado1)

#verificando si hay algun numero en comun 
resultado = conjunto3.isdisjoint(conjunto4) #si solo un dato es igual da falso si son totalmente distintos devuelve True

print(resultado)

resultado = conjunto3.isdisjoint(conjunto5) 

print(resultado)