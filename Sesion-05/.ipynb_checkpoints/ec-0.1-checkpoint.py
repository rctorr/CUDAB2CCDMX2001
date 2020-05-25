import numpy as np


def main():
    """ Función principal del script """
    # Generando la matriz con los datos de nuestra 
    # ecuación ax = b
    a = np.array([[2, 1, -3], [5, -4, 1], [1, -1, -4]])
    b = np.array([7, -19, 4])

    # Usando el submodulo linalg y la función solve
    x = np.linalg.solve(a, b)

    # Imprimiendo resultado
    print("El vector solución es:", x)

    # Realizando el producto punto entre a y x
    b1 = np.dot(a, x)
    
    # Comprobando si son iguales o casi iguales
    print("b original:", b)
    print("b calculado:", b1)
    ok = np.allclose(b, b1)
    if ok:
        print("Resultado correcto")
    else:
        print("No seas zope!")
        
    # Guardando resultado en archivo 
    # solucion.txt
    nomarch = "solucion.txt"
    np.savetxt(nomarch, b1, fmt="%d")
    print(
        "La solución se ha guardado en",
        nomarch
    )

if __name__ == "__main__":
    main()