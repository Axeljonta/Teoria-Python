#METODOS DE CADENA (string methods)

# Metodos son funciones aplicadas a objetos 

string1 = "Axel"
string2 = "sos un capo"
string3 = "24"
num= 1
# nos devuelve todos los metodos que hay para el dato que le pasemos 
print(dir(string1))

#convierte a string 
var = str(num)

# convierte mayusculas
resultado = string1.upper() 

# convierte minuscula 
resultado1 = string1.lower()

# solo la primera letra mayuscula
resultado2 = string2.capitalize()
print(resultado)

# devuelve la posicion de lo que le pasemos si no encuentra devuelve -1
resultado3 = string2.find("un")

# si no hay coincidecias devuelve excepcion
resultado4 = string2.index("u")

# devuelve true si es numerico aunque sea string
resultado5 = string3.isnumeric()

# true si es alphanumerico si hay espacios false
resultado6 = string3.isalpha()

# cuenta la cantidad de veces que esta lo que pasemos 
resultado7 = string2.count("s")

# cuanta los caracteres tiene una cadena, no es un metodo es una funcion
resultado8 = len(string2)

# verificamos si una cadena empieza con otra cadena dada, devuelve booleano
resultado9 = string2.startswith('sos') 

# verificamos si una cadena termina con otra cadena dada, devuelve booleano
resultado10 = string2.endswith('sos')

# si el valor 1 se encuentra en la cadena original, reemplaza valor 1 x valor 2
resultado11 = string2.replace("capo", "pete") 

# separa cadena con la cadena que le pasemos devuelve lista o matriz
resultado12 = string2.split(" ")

#slicing 
cadena = '0123456789'

print(cadena[1:4])

#------------------------------------------------------------