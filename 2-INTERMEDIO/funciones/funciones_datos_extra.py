#creando una funcion de 3 argumentos
def frase (nombre, apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizabdo keyword arguments 
frase_resultado = frase(adjetivo='boludo', nombre='Axel', apellido='Jontade')

#creando una funcion con un parametro opcional y un valor por defecto
def frase2 (nombre, apellido,adjetivo = 'Capo') :
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'


frase_resultado2 = frase2(adjetivo='boludo', nombre='Axel', apellido='Jontade')
