#METODOS DE LISTA (list methods)

# crea una lista es una funcion list() si o si hay que poner []
lista = list(["Axel", 24, "Jontade"])

# cuenta la cantidad de elementos de una lista
cantidad_elemntos = len(lista)

# agrega un elemento a la lista
lista.append('Argentino')

# agrega un elemeno a la lista en el indice especificado
lista.insert(1, 1.80)
 
# agrega varios elementos a la lista
lista.extend([True, 2000])

# elimina un elemento a una lista, pide indice y devulve valor si ponemos -1 elimina el ultimo elemento de la lista -2 el anteultimo y asi sucesivamente
lista.pop(4)

# remueve un elemnto de una lista por su valor
lista.remove(2000)

# elimina todos los elementos de una lista
# lista.clear()

# ordena una lista de menor a mayor, no tiene que tener strings
lista1=[True,34,12,False,235]
lista1.sort()
lista1.sort(reverse=True)#ordena una lista de mayor a menor

# invierte los elementos de una lista
lista.reverse()

# verifica si un elemento esta en la lista, nos devuelve el indice donde se encuentra 
elemnto_encontrado= lista1.index(12)

# en tuplas solo podemos buscar elemntos y usar index 
# en los conjuntos podemos limpierlos eleminar pero no pudemos usar el index

#------------------------------------------------------------