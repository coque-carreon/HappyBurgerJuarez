import json
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    encabezado_pagina = " Happy Burger - Pedidos"
    titulo_pagina = "Happy Burger - Lista de pedidos"
    pedidos = obtenerJSON("pedidos.json")
    return render_template("lista_pedidos.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        pedidos = pedidos)
    
@app.route('/datos/pedido/<id>')
def datos_pedido(id):
    encabezado_pagina = "Datos de pedido"
    pedidos = obtenerJSON("pedidos.json")
    pedido_encontrado = None
    titulo_pagina = None
    for pedido in pedidos:
        if pedido['id'] == int(id):
            pedido_encontrado = pedido
            titulo_pagina = "Datos de " + pedido_encontrado['name']
            break
    
    return render_template("datos_pedido.html", 
                        encabezado_pagina = encabezado_pagina, 
                        titulo_pagina = titulo_pagina,
                        pedido_encontrado = pedido_encontrado)
    
def obtenerJSON(nombre_archivo ):
    datos = {}
    try:
        with open(nombre_archivo) as archivo:
            datos = json.load(archivo)
    except Exception as e:
        print('Error al leer el archivo: {}'.format(e))
    return datos