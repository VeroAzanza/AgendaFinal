class vistaA:

	def menuA(self):
		print("--------------- AGENDA ---------------")
		print("1. Abrir agenda")
		print("2. Modificar agenda")
		print("3. Cerrar agenda")
		return int(input())

	def todo(self,contactos):
		if contactos != None:
			c = "CONTACTOS"
			print(c.center(80," "))
			for x in contactos:
				print(x)
		elif contactos == None:
			contacto = "No existen contactos"
			c = "CONTACTOS"
			print(c.center(80," "))
			print("\n",contacto,"\n")
			
	def modificacionA(self):
		print("\n")
		print("1. Agregar contacto")
		print("2. Modificar contacto")
		print("3. Eliminar todo")
		return int(input())