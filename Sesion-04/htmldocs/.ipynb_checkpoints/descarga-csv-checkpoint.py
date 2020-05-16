import requests


def main():
    """ Función principal """
    url = "http://localhost:8080/csv"
    
    # Obtener la respuesta del servidor
    respuesta = requests.get(url)
    nomarch = "archivos.csv"
    
    if respuesta.status_code == 200:  # ok?
        with open(nomarch, "wb") as da:
            da.write(respuesta.content)
    else:
        print("Error:", respuesta.status_code)


if __name__ == "__main__":
    main()