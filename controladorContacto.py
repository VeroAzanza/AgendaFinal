from modeloContacto import *
from vistaContacto import *
from controladorAgenda import *

class controladorC:

	def __init__(self):
		self.__vistaContacto = vista()
		self.mostrarMenu()

	def mostrarMenu(self):
		opcion = self.__vistaContacto.menu()
		if opcion == 1:
			self.agregar()
		elif opcion == 2:
			self.busca()
		elif opcion == 3:
			self.modificar()
		else:
			self.atras()


	def agregar(self):
		dato = self.__vistaContacto.datos()
		c = contacto(dato["nombre"],dato["telefono"],dato["email"])
		c.añadir()
		r = "Contacto añadido exitosamente"
		self.__vistaContacto.respuesta(r)
		self.mostrarMenu()

	def busca(self):
		dato = self.__vistaContacto.datos()
		c1 = contacto(dato["nombre"],dato["telefono"],dato["email"])
		c1.buscar()
		self.__vistaContacto.respuesta(c1)
		self.mostrarMenu()

	def modificar(self):
		eleccion = self.__vistaContacto.modificacion()
		if eleccion == 1:
			dato = self.__vistaContacto.datos()
			c2 = contacto(dato["nombre"],dato["telefono"],dato["email"])
			r = self.__vistaContacto.numero()
			c2.editarContacto(r)
			self.__vistaContacto.respuesta(c2)
			self.mostrarMenu()
		else:
			dato = self.__vistaContacto.datos()
			p = contacto(dato["nombre"],dato["telefono"],dato["email"])
			p.eliminarContacto()
			e = "Contacto eliminado"
			self.__vistaContacto.respuesta(e)
			self.mostrarMenu()

	def atras(self):
		controladorA()

controladorC()