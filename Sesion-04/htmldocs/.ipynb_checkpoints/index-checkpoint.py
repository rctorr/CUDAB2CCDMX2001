from bottle import route, run, HTTPResponse
import csv
import io
import lc

@route("/hola")
def hola():
    """ función principal del script """
    return "Hola Python"

@route("/")
def index():
    """ Función para responder la petici´on GET / """
    
    # Leer el contenido de index.html
    with open("index.html") as da:
        pagina = da.read()
    
    # Obtener la lista de archivos
    carpeta = lc.Carpeta(".")
    carpeta.obtiene_entradas()
    # Integrar la lista con el html
    tabla = "<table>\n"
    for ent in carpeta.entradas:
        linea = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(*ent)
        tabla += linea
    tabla += "</table>\n"
    # Insertando la tabla en la pagina
    pagina = pagina.replace("{TABLA}", tabla)
    
    return pagina

@route("/json")  # GET /json
def apijson():
    """ Atiende la petición GET /json """
    # Obtener la lista de archivos
    carpeta = lc.Carpeta(".")
    carpeta.obtiene_entradas()
    # Construir la lista de entradas de tipo dict() 
    entradas = [
        {"nombre": e[0], "tamanio":e[1], "fecha": e[2]}
        for e in carpeta.entradas
    ]
    # Integrar la lista de entradas al dict()
    dictArchivos = {"Archivos":entradas}
    
    return dictArchivos

@route("/csv")
def apicsv():
    """ Atiende la petición GET /csv """
    # Obtener la lista de archivos
    carpeta = lc.Carpeta(".")
    carpeta.obtiene_entradas()
    # Agregando fila de encabezados
    encabezados = ["nombre", "Tamaño", "Fecha"]
    entradas = [encabezados]
    entradas += carpeta.entradas
    
    # Construir la lista en un archivo CSV en memoria (RAM)
    da = io.StringIO()
    csv_writer = csv.writer(da)
    csv_writer.writerows(entradas)
    # Reinicando índice del archivo
    da.seek(0)
    # Personalizar encabezados de respuesta del HTTP
    h = {}
    h["content-type"] = "text/csv"
    h["Content-Disposition"] = "attachment;filename=archivos.csv"
    
    
    return HTTPResponse(
        body=da.read(),
        status=200,  # ok
        headers=h
    )


run(host='localhost', port=8080, debug=True)
