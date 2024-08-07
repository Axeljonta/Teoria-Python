
#usamos el as para poder trabajar el archivo, la w es un permiso de escriturqa asi podemos escribir en el archivo
#si no encuentra ningun archivo con w lo crea
with open('3-SEMI_AVANZADO/txt/texto.txt','w', encoding='UTF-8') as archivo:
      
    #sobreescribiendo el archivo 
    #archivo.write('Te borre todo jaja')
    
    #Si lo usamos mas de una vez se acumula no se sobreeescriben entre si
    #archivo.writelines(['Hola qur tal?\n','Todo mal con vos']) 
      
    #leyendo archivo 
    #contenido = archivo.read() 
    
    #mostrando archivo
    print (contenido)
    
    #no hace falta cerrar archivo 