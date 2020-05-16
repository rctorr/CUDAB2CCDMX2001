from bs4 import BeautifulSoup, element
import requests


def obtiene_pagina(nomarch):
    """ Lee la página desde nomarch """
    with open(nomarch, 'r') as html:
        pagina = html.read()
    return pagina

def navega_pagina(pagina):
    """
    Imprime el contenido de la página en forma de árbol
    """
    sopa = BeautifulSoup(pagina, features="html.parser")
    # Content tiene una lista de todos los elementos
    html = sopa.contents[0]
    body = html.contents[3]
    ecopyramyd = body.contents[1]
    # ahora revisamos los elementos de div.ecopyramyd
    for ul in ecopyramyd.children:
        # NavigableString es un string entre tags, se debe ignorar
        if type(ul) == element.NavigableString:
            continue
        print(ul['id'].capitalize())
        for child in ul.children:
            if type(child) == element.NavigableString:
                continue
            li = child.contents[0]
            name = li.nextSibling.text.capitalize()
            number = li.nextSibling.nextSibling.nextSibling.text.capitalize()
            print("\t-{}: {}".format(name, number))

def main():
    """ Función principal del script """
    pagina = obtiene_pagina("piramide.html")
    navega_pagina(pagina)

if __name__ == '__main__':
    main()
