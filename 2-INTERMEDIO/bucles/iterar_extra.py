colores = ['azul', 'rojo', 'violeta', 'verde', 'amarillo', 'naranja']
cadena = 'HOLA MUNDO!!!'
numeros = [3 , 2 , 72 , 11]

#evitando que se itere un elemento 
for i in colores:
    if i == 'verde':
        continue
    print(f'1- me gusta el color {i}')

#evitar que el bucle continue (el else no se ejecuta tampoco)
for i in colores:
           print(f'2- me gusta el color {i}')
           if i == 'amarilloo':
               break
else:
            print('listo')
 
#recorrer una cadena de texto (string)
for i in cadena:
    print(i)
    
#for en una linea de codigo 
numeros_duplicados = [i*2 for i in numeros]
print (numeros_duplicados)

    
    
    
  
    