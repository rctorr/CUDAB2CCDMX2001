from bs4 import BeautifulSoup
import os
import requests

def main():
    """ función principal del script """
    url = "https://unsplash.com"

    # Obtener contenido de página    
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        sopa = BeautifulSoup(respuesta.content)
        imagenes = sopa.find_all("img")
        print(imagenes)
        numfoto = 1
        for img in imagenes:
            if "photo" in img["src"]:
                imagen = requests.get(img["src"])
                if imagen.status_code == 200:
                    nomfoto = "foto" + str(numfoto) + ".jpg"
                    nomfoto = os.path.join("img", nomfoto)
                    with open(nomfoto, "wb") as da:
                        da.write(imagen.content)
                    numfoto += 1
    else:
        print("Error:", respuesta.status_code)


if __name__ == "__main__":
    main()