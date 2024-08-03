diccionario = {
    'nombre': 'Axel',
    'apellido': 'Jontade',
    'sueldo': 850000
}

#nos va a devolver solo las key
for i in diccionario:
    print(i) 
    
#nos devuelve clave valor
for i in diccionario.items():
    key = i[0]
    value = i[1]
    print(f'Key: {key} value: {value}')