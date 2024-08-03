#OPERADORES

#----------------------------------------------

#ARITMETICOS

suma = 2+1
resta = 2-1

multi = 2*4
division = 12/5

exponente = 10**10

division_baja = 12//5

resto = 12%5

tipo_de_dato = type(division) #devuelve el tipo de dato 

#----------------------------------------------

#COMPARACION 

es_igual_que = 5 == 6

distinto_que = 5 != 6 

mayor_que = 5 > 6 

menor_que = 5 < 6

mayor_igual_que = 5 >= 6 

menor_igual_que = 5 <= 6 

#Devuelven datos booleano 

#----------------------------------------------

#CONDICIONALES

#if-else

if True:
    i="hola"
    #se ejecuta el codigo si es False no 
else:
    i="chau"
    #se ejecuta si el if es False

#elif 
ingreso = 1500

if ingreso > 2000: 
    print("Estas bien en cualquier lado pa")
elif ingreso > 700:  # si no se cumple el if le damos una segunda instancia
    print("Estas bien en Argentina")
else:
    print("sos pobre")

#----------------------------------------------

#LOGICOS

#AND 

Resultado = True & True #True
Resultado1 = False & True #Flase
Resultado3 = False & False #False

#OR

Resultado4 = True | True #True
Resultado5 = False | True #True
Resultado6 = False | False #False

#NOT

Resultado7 = not True #False
Resultado8 = not False  #True 


