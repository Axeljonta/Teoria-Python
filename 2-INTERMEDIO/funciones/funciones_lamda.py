#crando una funcion lamda (es como crear una funcion anonima)
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(3))

#otro ejemplo 
numeros = [2,9,46,21,1,7,98,15,17,19,12,8,4,6]
numeros_pares = filter(lambda n: n%2 == 0, numeros)
print(list(numeros_pares))
