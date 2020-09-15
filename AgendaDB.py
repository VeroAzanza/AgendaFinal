import pyodbc


class BaseDeDatos:

	def __init__(self,name,server = 'localhost\SQLEXPRESS',
				driver="SQL Server Native Client 11.0"):
		self.__name = name
		self.__server = server
		self.__driver = driver
		self.__conexion = None
		self.__datos = None
		self.__cursor = None

	def conectar(self):
		self.__conexion = pyodbc.connect("DRIVER={"+self.__driver+"};"
                                  "Server="+self.__server+";"
                                  "DATABASE="+self.__name+";"
                                  "Trusted_Connection=yes;")
	def cursor(self):
		self.__cursor = self.__conexion.cursor()
	
	def commit(self,query):
		select = query.count('SELECT')
		if select == 0:
			self.__conexion.commit()
	
	def cerrar(self):
		self.__conexion.close()
	
	def obtener_datos(self,query):
		select = query.count('SELECT')
		if select > 0:
			self.__datos = self.__cursor.fetchall()

	def consulta(self,q,v=None):
		if v:
			self.__cursor.execute(q,v)
		else:
			self.__cursor.execute(q)
	
	def ejecutar(self,query,values = None):
		self.conectar()
		self.cursor()
		self.consulta(query,values)
		self.commit(query)
		self.obtener_datos(query)
		self.cerrar()

		return self.__datos