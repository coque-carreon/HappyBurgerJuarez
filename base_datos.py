import sqlite3 
import os

class BaseDatos:
    
    def __init__(self, nombreBaseDatos):
        self.nombreBaseDatos = nombreBaseDatos
        
    # Método para crear base de datos
    def crearBaseDatos(self):
        try:
            conn = sqlite3.connect(self.nombreBaseDatos) 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))
        
    # Método para verificación de base de datos
    def verificarBaseDatosExiste(self):
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False
    
    # Método para creación de tabla de clientes
    def crearTablaclientes(self):
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE clientes
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_cliente TEXT NOT NULL,
            edad TEXT NOT NULL,
            ciudad TEXT NOT NULL,
            telefono TEXT NOT NULL
            );''')
        
        conexion.close()
        
     # Método para creación de tabla de insumos
    def crearTablainsumos(self):
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE insumos
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_insumo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio TEXT NOT NULL,
            stock TEXT NOT NULL
            );''')
        
        conexion.close()
        
        
    # Método que abre la conexion a la base de datos
    # y marca error si no existe
    
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos) 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))