from base_datos import BaseDatos
import sqlite3

class AdministracionInsumos:
    
    baseDatos = None
    autenticacion = None
    
    def __init__(self):
        self.baseDatos = BaseDatos('insumos.db')
        #self.autenticacion = Autenticacion()
        if not self.baseDatos.verificarBaseDatosExiste():
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablainsumos()

    def mostrarListaInsumos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM insumos")     
            insumos = cursor.fetchall()
            if len(insumos) > 0:
                print("Lista de insumos disponibles: ")
                print("------------------------------------")
                for id,nombre_insumo,descripcion,precio,stock in insumos:
                    print('id: {}, nombre del insumo: {}, descripción: {}, precio: {}, stock: {}'
                        .format(id, nombre_insumo, descripcion, precio, stock))
                print("------------------------------------")
            else:
                print("No hay insumos que mostrar")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla insumos", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def agregarInsumo(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            nombre_insumo,descripcion,precio,stock = self.ingresarDatosInsumo()
            valores = (nombre_insumo, descripcion, precio, stock)
            sql = ''' INSERT INTO insumos(nombre_insumo,descripcion,precio,stock)
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

    def modificarInsumo(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM insumos")     
            insumos = cursor.fetchall()
            if len(insumos) > 0:
                
                print("Lista de insumos para modificar:")
                self.mostrarListaInsumos()
                print("----------------------------------")
                id_insumo = self.ingresarID("Ingresa el id del insumo a modificar \n")
                
                encontrar_insumo = cursor.execute("SELECT * FROM insumos WHERE id = ?", (id_insumo,))    
                insumo = encontrar_insumo.fetchone()
                if insumo :
                    nombre_insumo,descripcion,precio,stock = self.ingresarDatosInsumo()
                    sql = ''' UPDATE insumos SET nombre_insumo = ?, descripcion = ?, precio = ?, stock = ? WHERE id = ? '''
                    datos_insumo = (nombre_insumo,descripcion,precio,stock,id_insumo)
                    cursor.execute(sql,datos_insumo)
                    conexion.commit()
                    print("Registro modificado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            else:  
                print("No hay insumos para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as e:
            print('Error al intentar modificar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def eliminarInsumo(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM insumos")     
            insumos = cursor.fetchall()
            if len(insumos) > 0:
            
                print("Lista de insumos para eliminar:")
                self.mostrarListaInsumos()
                print("------------------------------------")
                id_insumo = self.ingresarID("Ingresa el id del insumo a eliminar \n")
                
                encontrar_insumo = cursor.execute("SELECT * FROM insumos WHERE id = ?", (id_insumo,))     
                if len(encontrar_insumo.fetchall()) == 1:
                    sql = ''' DELETE FROM insumos WHERE id = ? '''
                    cursor.execute(sql,(id_insumo,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            
            else:  
                print("No hay insumos para eliminar")
                print("------------------------------------")
                
        except sqlite3.Error as e:
            print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def ingresarID(self,mensaje):
        id_insumo = 0
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                id_insumo = int(input( mensaje ))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar el id del insumo: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_insumo

    def ingresarDatosInsumo(self):
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                nombre_insumo = input("Ingresa el nombre del insumo \n")
                descripcion = input("Ingresa descripción del insumo \n")
                precio = float(input("Ingresa el precio del insumo \n"))
                stock = int(input("Ingresa el stock del insumo \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return nombre_insumo,descripcion,precio,stock
