
#Ejercicio 1-1
#promedio de horas duracion de los distintos cursos online 

def redondear(i): 
    i_str = str(i)
    if '.' in i_str:
        entero, decimal = i_str.split('.') 
        
        if len(decimal) > 2: 
            i = round(i,2)
    return i


otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
mi_curso = 1.5

#Tiempo de los videos en crudos 

crudo_promedio = 5 
crudo_mio = 3.5

#Driferencia de duracion 

diferencia_min = redondear(100 - mi_curso / otros_cursos_min * 100)
diferencia_max = redondear(100 - mi_curso / otros_cursos_max * 100)
diferencia_prom = redondear(100 - mi_curso / otros_cursos_prom*100)

#Calculando el porcentaje de tiempo vacio removido 

tiempo_vacio_promedio = redondear(100 - otros_cursos_prom / crudo_promedio * 100)
tiempo_vacio_mio = redondear(100 - mi_curso * 1000 // crudo_mio / 10) 

#Mostrado las diferencias de duracion (ejercicio A)

print('----------------------------------------------------')
print(f'Tu curso dura {diferencia_min}% menos que el mas rapido')
print(f'Tu curso dura {diferencia_max}% menos que el mas rapido')
print(f'Tu curso dura {diferencia_prom}% menos que el mas rapido')

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)

print('----------------------------------------------------')
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% del tiempo vacio')
print(f'Un curso mio elimina un {tiempo_vacio_mio}% del tiempo vacio')

#Mostrando diferencias si los cursos duraran 10hs 

print('----------------------------------------------------')
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom * 100 // mi_curso / 10} horas de otros curso')
print(f'Ver 10 horas de otros curso equivale a ver {mi_curso * 100 // otros_cursos_prom / 10} horas de este curso')

#Ejercicio 1-2

print('----------------------------------------------------')
frase = input('Decime una frase, y calcula cuanto tardarias en decirla: ')
palabras_separadas = frase.split(' ') 
cantidad_palabras = len(palabras_separadas)

print('----------------------------------------------------')
print(f'Dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} segundos en decirlo.')
print(f'Axel tardaria {redondear(cantidad_palabras/2/1.3)} segundos en decirlo.')
print('----------------------------------------------------')
if cantidad_palabras > 120:
    print('Para no te pedi la biblia!!!')

