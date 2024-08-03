#creando diccionario con dict()
diccionario = dict(nombre = 'Axel', apellido = 'Jontade')

#la listas no pueden ser claves, las tuplas tambien, ni un conjunto a menos que usemos frozenset()
diccionario = {frozenset(['Axel' , 'Rancio']):'y si'}

#crendo diccionarios con fromkeys()
diccionario = dict.fromkeys('nombre') #por defecto el segundo valor es none por eso si no ponemos [] itera el primer dato
diccionario = dict.fromkeys(['nombre','apellido','seguidores'])
diccionario = dict.fromkeys(['nombre','apellido','seguidores'], 'No se')

