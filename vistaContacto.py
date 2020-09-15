class vista:

    def menu(self):
        m = "MENU"
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Salir de contactos")
        return int(input("Ingrese opción: "))

    def datos(self):
        print("Ingrese datos del contacto: nombre, telefono y email(opcional):")
        nombre = input()
        telefono = input()
        email = input()
        cont = {"nombre": nombre,"telefono": telefono,"email": email}
        return cont

    def modificacion(self):
        print("\n")
        print("1. Modificar número de teléfono")
        print("2. Eliminar contacto","\n")
        opcion = int(input())
        return opcion

    def respuesta(self,respuesta):
        r = "RESPUESTA"
        print(r.center(80," "))
        print("\n",respuesta,"\n")
