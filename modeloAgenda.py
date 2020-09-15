from AgendaDB import BaseDeDatos

class agenda:

	__NombreBase = BaseDeDatos(name = 'Agenda')
	__tabla = 'contactos'

	@classmethod
	def mostrarTodo(cls):
		query = "SELECT * FROM " + agenda.__tabla
		return agenda.__NombreBase.ejecutar(query)
	
	@classmethod	
	def borrarTodo(cls):
		query = "DELETE FROM " + agenda.__tabla
		p = agenda.__NombreBase.ejecutar(query)
