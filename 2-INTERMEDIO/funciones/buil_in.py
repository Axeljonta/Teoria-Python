numeros = [4,32,96,84,51,42,75,84,92,63]

#max() encontrando numero mayor
resultado_max = max (numeros)

#min() encontrando numero menor
resultado_min = min (numeros)

#round() redondeando decimales
resultado_round = round(12.5687842198494,2)
print (resultado_round)

#bool() retorna false si : 0, false, vacio, none. true si: distinto a 0, cadena, datos no vacios
resultado_bool = bool(None)#falso

#all() return true, si todos los valores son verdaderos
resultado_all = all([0, 'hola', True])

#sum() soma todos los numeros de un iterable 
resultado_sum = sum(numeros) 
print(resultado_sum)