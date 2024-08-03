animales = ['perro', 'gato', 'cocodrilo', 'loro', 'conejo'] 
numeros = [34, 12, 32, 51, 74, 2, 11, 62, 102]
 
#iterando listas
for animal in animales: 
    print(f'Ahora la variable aniaml es igual a: {animal}') 

for numero in numeros:
    print(numero*2)

#iterando 2 listas al mismo tiempo, tienen que ser del mismo tamaño cuando una lista se termina se termina el for por mas que en otra lista haya mas datos
for numero,animal in zip (animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')
 
#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)  
for num in range(len(numeros)):
    print('esto esta mal')
 
#forma correcta, devuelve una tupla esta la forma correcta de desempaquetarla 0   
for key, value in enumerate(numeros):
    indice = key
    valor = value
    print(key, value)
#el else se va a ejecutar cuando se termina de realizar el bucle 
else: 
    print('el bucle termino')
    
#todo funciona igual para tuplas, listas y conjuntos

