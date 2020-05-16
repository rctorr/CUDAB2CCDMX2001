from bs4 import BeautifulSoup
import os
import requests


def main():
    """ Función principal """
    url = "https://unsplash.com"
    
    # Obtener el contenido
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        sopa = BeautifulSoup(respuesta.content)
        imagenes = sopa.find_all("img")
        numfoto = 0
        for img in imagenes:
            if "photo-" in img["src"]:
                # Obtener la foto a partir del src
                imgresp = requests.get(img["src"])
                if imgresp.status_code == 200:
                    nomfoto = os.path.join(
                        "img", "foto{}.jpg".format(numfoto))
                    with open(nomfoto, "wb") as da:
                        da.write(imgresp.content)
                    numfoto += 1        
    else:
        print("Error:", respuesta.status_code)


if __name__ == "__main__":
    main()