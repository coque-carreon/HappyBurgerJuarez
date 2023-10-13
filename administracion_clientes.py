from base_datos import BaseDatos
import sqlite3

class AdministracionClientes:
    
    baseDatos = None
    autenticacion = None
    
    # Definicion de base de datos y llamado de autenticacion
    
    def __init__(self):
        self.baseDatos = BaseDatos('clientes.db')
        #self.autenticacion = Autenticacion()
        if not self.baseDatos.verificarBaseDatosExiste():
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablaclientes()
            
    # Mostrar lista de clientes
    def mostrarListaClientes(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                print("Lista de clientes disponibles: ")
                print("------------------------------------")
                for id,nombre_cliente,edad,ciudad,telefono in clientes:
                    print('id: {}, nombre del cliente: {}, edad: {}, ciudad: {}, teléfono: {}'
                        .format(id, nombre_cliente, edad, ciudad, telefono))
                print("------------------------------------")
            else:
                print("No hay clientes que mostrar")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla clientes", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    # Agregar cliente a la base de datos clientes
    def agregarClientes(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            nombre_cliente,edad,ciudad,telefono = self.ingresarDatosCliente()
            valores = (nombre_cliente, edad, ciudad, telefono)
            sql = ''' INSERT INTO clientes(nombre_cliente,edad,ciudad,telefono)
                    VALUES(?,?,?,?) '''
                    
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------------")
        except sqlite3.Error as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    # Modifica el cliente si es que existe, si no, nos indica que no existe
    def modificarCliente(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                
                print("Lista de clientes para modificar:")
                self.mostrarListaClientes()
                print("----------------------------------")
                id_cliente = self.ingresarID("Ingresa el id del cliente a modificar \n")
                
                encontrar_cliente = cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))    
                cliente = encontrar_cliente.fetchone()
                if cliente :
                    nombre_cliente,edad,ciudad,telefono = self.ingresarDatosCliente()
                    sql = ''' UPDATE clientes SET nombre_cliente = ?, edad = ?, ciudad = ?, telefono = ? WHERE id = ? '''
                    datos_cliente = (nombre_cliente,edad,ciudad,telefono,id_cliente)
                    cursor.execute(sql,datos_cliente)
                    conexion.commit()
                    print("Registro modificado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            else:  
                print("No hay clientes para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as e:
            print('Error al intentar modificar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    # Método para la eliminación de clientes
    def eliminarCliente(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
            
                print("Lista de clientes para eliminar:")
                self.mostrarListaClientes()
                print("------------------------------------")
                id_cliente = self.ingresarID("Ingresa el id del cliente a eliminar \n")
                
                encontrar_cliente = cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))     
                if len(encontrar_cliente.fetchall()) == 1:
                    sql = ''' DELETE FROM clientes WHERE id = ? '''
                    cursor.execute(sql,(id_cliente,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            
            else:  
                print("No hay clientes para eliminar")
                print("------------------------------------")
                
        except sqlite3.Error as e:
            print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    # Método para buscar el ID y si esta correctamente capturado
    def ingresarID(self,mensaje):
        id_cliente = 0
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                id_cliente = int(input( mensaje ))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar el id del cliente: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_cliente

    # Método para capturar los datos del cliente
    def ingresarDatosCliente(self):
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                nombre_cliente = (input("Ingresa el nombre del cliente \n"))
                edad = int(input("Ingresa edad del cliente \n"))
                ciudad = (input("Ingresa la ciudad del cliente \n"))
                telefono = (input("Ingresa el telefono del cliente \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return nombre_cliente,edad,ciudad,telefono
