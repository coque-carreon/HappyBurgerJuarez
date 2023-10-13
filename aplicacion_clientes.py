from administracion_clientes import AdministracionClientes

class AplicacionClientes:
    
    def __init__(self) -> None:
        self.iniciarAplicacion()
        
        # Menu principal
    def iniciarAplicacion(self):
        clientes = AdministracionClientes()
        print("------------------------------------")
        print("Bienvenido al módulo de Clientes")
        salir_programa = False
        while not salir_programa:
            print("Menú de clientes")
            print(""" 
                1.- Mostrar lista de clientes
                2.- Agregar clientes
                3.- Modificar clientes
                4.- Eliminar clientes
                5.- Salir del programa
                """)
            opcion = int(input("Indica una opción del menú: "))
            if opcion == 1:
                clientes.mostrarListaClientes()
            elif opcion == 2:
                clientes.agregarClientes()
            elif opcion == 3:
                clientes.modificarCliente()
            elif opcion == 4:
                clientes.eliminarCliente()
            if opcion == 5:
                print("Salida del programa, hasta luego ")
                salir_programa = True
        return salir_programa
                
# Objeto Aplicacion
#sistema_clientes = AplicacionClientes()
