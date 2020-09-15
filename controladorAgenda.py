from modeloAgenda import *
from vistaAgenda import *
from modeloContacto import *
from vistaContacto import *

class controladorA:

	def __init__(self):
		self.__vistaA = vistaA()
		self.menuAgenda()

	def menuAgenda(self):
		op = self.__vistaA.menuA()
		if op == 1:
			self.mostrar()
		elif op == 2:
			self.entrarAgenda()
		elif op == 3:
			self.cerrar()

	def mostrar(self):
		a = agenda()
		personas = a.mostrarTodo()
		self.__vistaA.todo(personas)
		self.menuAgenda()

	def entrarAgenda(self):
		opcion = self.__vistaA.modificacionA()
		if opcion == 1:
			dato = vista()
			d = dato.datos()
			p = contacto(d["nombre"],d["telefono"],d["email"])
			p.añadir()
			self.menuAgenda()
		elif opcion == 2:
			op = vista()
			opcion = op.modificacion()
			if opcion == 1:
				dato = vista()
				d = dato.datos()
				p = contacto(d["nombre"],d["telefono"],None)
				p.editarContacto()
				self.menuAgenda()
			elif opcion == 2:
				dato = vista()
				d = dato.datos()
				p = contacto(d["nombre"],None,None)
				p.eliminarContacto()
				self.menuAgenda()
		else:
			a = agenda()
			eliminados = a.borrarTodo()
			self.__vistaA.todo(eliminados)

	def cerrar(self):
		pass

controladorA()