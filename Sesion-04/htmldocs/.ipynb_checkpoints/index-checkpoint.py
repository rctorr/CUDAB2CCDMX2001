from bottle import route, run
import lc

@route("/hola")
def hola():
    """ funci´on principal del script """
    return "Hola Python"

@route("/")
def index():
    """ Funci´on para responder la petici´on GET / """
    
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

@route("/json")
def apijson():
    """ Atiende la petici´on GET /json """
    return { "Archivos":[{"mensaje": "Hola JSON"}, {"mensaje": "Hola JSON"}]}


run(host='localhost', port=8080, debug=True)
