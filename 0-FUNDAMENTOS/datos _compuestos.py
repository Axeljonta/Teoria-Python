#DATOS COMPUESTOS

#-----------------------------------------------------

#LISTAS
#          0      1    2
lista = ["Axel", 24, 1.85]

lista [2] = "MAQUINA" 

print(lista, lista [2])
#la lista se puede modificar 

#-----------------------------------------------------

#TUPLA 
tupla = ("Axel", 24, 1.85)

#NO SE PUEDE MODIFICAR, para mostrar se usan corchetes
tupla[1] 
print(tupla)

#-----------------------------------------------------

#conjunto 
# igual que la lista solo que 
# no muestra valores repetidos
# no podemos acceder una posicion por el indice ej conjunto[1] = error 
# solo por bucles se puede acceder a un elemento especifico

conjunto = {"Axel", 24, 1.85, "Axel"}
print(conjunto)

#-----------------------------------------------------

#diccionario 
# como lista pero nosotros le ponemos el nombre  (key) a los valores ( value)
diccionario= {
    # key    :   value   
    "nombre" : "Axel",
    "apellido" : "Jontade", 
    "edad": 24
}

print(diccionario["apellido"])

#------------------------------------------------------