from administracion_insumos import AdministracionInsumos

class AplicacionInsumos:
    
    def __init__(self):
        self.iniciarAplicacion()
        
    def iniciarAplicacion(self):
        insumos = AdministracionInsumos()
        print("------------------------------------")
        print("Bienvenido al sistema de Insumos")
        salir_programa = False
        while not salir_programa:
            print("Menú de Insumos")
            print(""" 
                1.- Mostrar lista de insumos
                2.- Agregar insumo
                3.- Modificar insumo
                4.- Eliminar insumo
                5.- Salir del programa
                """)
            opcion = int(input("Indica una opción del menú: "))
            if opcion == 1:
                insumos.mostrarListaInsumos()
            elif opcion == 2:
                insumos.agregarInsumo()
            elif opcion == 3:
                insumos.modificarInsumo()
            elif opcion == 4:
                insumos.eliminarInsumo()
            if opcion == 5:
                print("Volver a MENU PRINCIPAL ")
                salir_programa = True
        return salir_programa
                
#sistema_insumos = AplicacionInsumos()
    