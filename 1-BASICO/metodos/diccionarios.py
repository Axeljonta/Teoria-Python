#METODOS DE DICCIONARIOS (dic methods)

diccionario= { 
    "nombre" : "Axel",
    "apellido" : "Jontade", 
    "edad": 24
}

# devuelve las claves ( tambien nos sirve para iterar)
claves= diccionario.keys()

# devuelve el valor de una clave 
claves1= diccionario.get('edad')# si no encuentra valor devuelve none
claves2= diccionario['nombre']#se puede hacer asi pero es mala practica ya que si no encuntra el valor devuelve un error

# elimina todos los elemntos
#diccionario.clear()

# elimina un elemnto
diccionario.pop('edad')

# para iterar el dic
dic_iterable= diccionario.items()
# nos devuelve un elemento iterable (que se puede recorrer el elemento para accceder c/u de los elemntos)

#------------------------------------------------------------