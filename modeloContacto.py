from AgendaDB import BaseDeDatos

class contacto:

	__NombreBase = BaseDeDatos(name = 'Agenda')
	__tabla = 'contactos'

	def __init__(self,nombre,telefono,email=None):
		self.__nombre = nombre
		self.__telefono = telefono
		self.__email = email

	def añadir(self):
		query = "INSERT INTO " + contacto.__tabla + "(nombre,telefono,email) VALUES (?,?,?)"
		values = (self.__nombre,self.__telefono,self.__email)
		persona = contacto.__NombreBase.ejecutar(query,values)

	def editarContacto(self):
		query = "UPDATE " + contacto.__tabla + " SET telefono = ? WHERE nombre = ?" 
		values = (self.__telefono,self.__nombre)
		p = contacto.__NombreBase.ejecutar(query,values) 

	def eliminarContacto(self):
		query = "DELETE FROM " + contacto.__tabla + "WHERE nombre = " + self.__nombre
		p = contacto.__NombreBase.ejecutar(query)

	def buscar(self):
		query = "SELECT nombre,telefono,email FROM " + contacto.__tabla + "WHERE nombre = " + self.__nombre
		return contacto.__NombreBase.ejecutar(query)