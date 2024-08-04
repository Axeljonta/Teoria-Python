#as es para renombrar el modulo 
import modulos_saludar as m_s

#importar una funcion especifica del modulo
from modulos_saludar import despedida

#llamando la funcion del  modulo 
saludo = m_s.saludar('Axel')
print(saludo)

#
chau = despedida('Lucas')
print(chau)





