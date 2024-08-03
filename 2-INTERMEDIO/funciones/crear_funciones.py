#creando una funcion simple
def saludar(nom):
    print(f'Hola {nom}!!!')
    
saludar('Julieta')
saludar('Axel')
saludar('Sofia') 

#crear una funcion que nos retorne valores 
def crear_contraseña(i): 
    listado = 'abcdefghijk'
    num = int(i[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{listado[c1]}{listado[c2]}{listado[c3]}{num*7 -2}'
    return (contraseña) 

user_input = input('Decime un numero, y te creo una contraseña: ')
password = crear_contraseña(user_input)
frase = f'Tu contraseña nueva es: {password}'
print(frase)


