archivo_txt = open('3-SEMI_AVANZADO/txt/texto.txt', encoding='UTF-8')

#solo se puede leer una vez

#Leer archivo completo 
#archivo = archivo_txt.read()

#leer linea por linea 
#lineas = archivo_txt.readlines()

#leer una sola linea 
linea = archivo_txt.readline(2)

#cerrar el archivo 
archivo_txt.close()

#print(archivo)

print(linea)

