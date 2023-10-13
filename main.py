#import requests
import subprocess
import webbrowser
from aplicacion_clientes import AplicacionClientes
from aplicacion_insumos import AplicacionInsumos

class Autenticacion:
    def __init__(self):
        self.is_login = False

    def verificarAutenticacion(self):
        while not self.is_login:
            usuario = input("Ingresar usuario: ")
            password = input("Ingresar contraseña: ")
            if usuario != 'admin' or password != '12345':
                print("Error de login")
            else:
                self.is_login = True

def menu_principal():
    autenticacion = Autenticacion()
    autenticacion.verificarAutenticacion()  # Llamada a la función verificarAutenticacion al inicio

    opcion = ""

    while opcion != "s":
        print("BIENVENIDOS AL HAPPY BURGER \n")
        print("a. Pedidos")
        print("b. Clientes")
        print("c. Insumos")
        print("s. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "a":
            # Ejecuta el servidor Flask en segundo plano
            servidor_flask = subprocess.Popen(['flask', '--app', 'server', 'run'])

            # Abre el enlace http listado
            webbrowser.open('http://127.0.0.1:5000/')

        elif opcion == "b":
            # Abre la aplicación ABC de Clientes
            print("MENÚ CLIENTES")
            aplicacion_clientes = AplicacionClientes()
            aplicacion_clientes.ejecutar()

        elif opcion == "c":
            # Abre la aplicación ABC de Insumos/Menú
            print("MENÚ INSUMOS")
            aplicacion_insumos = AplicacionInsumos()
            aplicacion_insumos.ejecutar()

        elif opcion == "s":
            print("Elegiste salir")

        else:
            print("La opción es inválida")

    # Cierra el servidor Flask antes de salir del menú
    if servidor_flask:
        servidor_flask.terminate()

# Inicia la ejecución del menú
menu_principal()
