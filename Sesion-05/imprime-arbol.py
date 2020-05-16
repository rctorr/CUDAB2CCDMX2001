from bs4 import BeautifulSoup, element
import requests


def obtiene_pagina(url):
    """ Obtiene la página desde la url """
    with open(url) as html:
        pagina = html.read()
        
    return pagina

def main():
    """ Función principal """
    url = "piramide.html"
    
    # Obtener el contenido desde un archivo
    pagina = obtiene_pagina(url)
    
    # Navegar en la página e imprimirla
    sopa = BeautifulSoup(pagina, features="html.parser")
    html = sopa.contents[0]
    body = html.contents[3]
    ecopyramyd = body.contents[1]
    for ul in ecopyramyd.children:  # hijos son: <ul>...</ul>
        if type(ul) == element.NavigableString:
            # si es un \n entonces brica la iteración y continua
            # con la siguiente.
            continue
        print(ul["id"].upper())
        for li in ul.children:
            if type(li) == element.NavigableString:
                # si es un \n entonces brica la iteración y
                # continua con la siguiente.
                continue
            nombre = li.contents[1].text
            valor = li.contents[3].text
            print("    -{}: {}".format(nombre, valor))
            

if __name__ == "__main__":
    main()