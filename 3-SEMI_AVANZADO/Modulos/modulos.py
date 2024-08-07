#as es para renombrar el modulo tambien sirve para renombrar funciones
import modulos_saludar as m_s

#importar una funcion especifica del modulo
from modulos_saludar import despedida

#llamando la funcion del  modulo 
saludo = m_s.saludar('Axel')
print(saludo)

#llamando solo a la funcion despedida 
chau = despedida('Lucas')
print(chau)






