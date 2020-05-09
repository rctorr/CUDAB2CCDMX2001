import csv
import json
import os
import time

## Modelo-Vista-Controlador (MVC)

## Modelo: obtiene datos
def obtiene_entradas(ruta):
    """
    Obtiene la lista de entradas de ruta y regresa una lista
    con el nombre y tamaño de cada una.
    """
    # Se obtiene el nombre de las entradas
    nombres = os.listdir(ruta)
    # Obtener el tamaño de cada uno de los elementos que
    # son archivos.
    # [
    #   ["/home/rctorr/python-analisis-datos/archivo1", 1234],
    #   ["/home/rctorr/python-analisis-datos/archivo2", 5678],
    #   ...
    # ]

    # Agregando ruta a los nombres
    # for i, n in enumerate(nombres):  # [(0, "arch1"), (1, "arch2"), ...]
    #    nombres[i] = os.path.join(ruta, n)
    nombres = [os.path.join(ruta, n) for n in nombres]

    entradas = []
    total = 0
    for n in nombres:
        fecha = os.path.getmtime(n)  # segundos
        fecha = time.ctime(fecha)  # str
        if os.path.isfile(n):  # path o ruta
            # -obtener el tamaño de n-
            # -agregarlo a la lista-
            tamanio = os.path.getsize(n)
            entrada = [n, tamanio, fecha]
            entradas.append(entrada)
            total += tamanio  # total = toal + tamanio
        else:
            # Entonces es un carpeta
            # -asignar tamaño igual cero-
            # -agregarlo a la lista-
            entrada = [n, 0, fecha]
            entradas.append(entrada)
            # total += 0  # si es cero, no tiene caso
            
    return entradas, total

# Vista: Genera resultado para el usuario
def imprime_entradas(entradas, total):
    """
    Imprime la lista de entradas en la salida estándar en
    forma tabular.
    """
    for e in entradas:
        print("{:30} {:10} {:24}".format(*e))
        
    print("{:30} {:10} {:24}".format("Total:",total,"bytes"))

def guarda_entradas(entradas, total, arch_salida):
    """
    Guarda la lista de entradas en el archivo arch_salida en
    forma tabular.
    """
    # da = open(arch_salida, "w")  # da= descriptor de archivo   
    # for e in entradas:
    #    da.write("{:60} {:10} {:24}\n".format(*e))
    # da.write("Total: {} bytes\n".format(total))
    # da.close()
    with open(arch_salida, "w") as da:
        for e in entradas:
            da.write("{:60} {:10} {:24}\n".format(*e))
        da.write("Total: {} bytes\n".format(total))

def guarda_entradas_csv(entradas, arch_salida_csv):
    """
    Guarda la lista de entradas en el archivo arch_salida en
    formato CSV.
    """
    with open(arch_salida_csv, "w", encoding="utf-8") as da:
        da_csv = csv.writer(da)
        da_csv.writerow(["Nombre", "Tamaño", "Fecha"])
        for e in entradas:
            da_csv.writerow(e)  # e = ["nomb", 1234, "fecha"]

def guarda_entradas_json(entradas, total, arch_salida_json):
    """
    Guarda la lista de entradas en el archivo arch_salida en
    formato JSON usando array.
    """
    with open(arch_salida_json, "w", encoding="utf-8") as da:
        json.dump(entradas, da, indent=4)

def guarda_entradas_json2(entradas, total, arch_salida_json):
    """
    Guarda la lista de entradas en el archivo arch_salida en
    formato JSON usando objetos.
    """
    with open(arch_salida_json, "w", encoding="utf-8") as da:
        json.dump(entradas, da, indent=4)

# Controlador: Manipular las funciones del Modelo y la Vista
def main():
    """
    Función principal del script
    """
    # ruta = "/home/rctorr/python-analisis-datos"
    ruta = "."
    arch_salida = "salida.txt"
    arch_salida_csv = "salida.csv"
    arch_salida_json = "salida.json"
    arch_salida_json2 = "salida2.json"
    
    entradas, total = obtiene_entradas(ruta)  # Nombre, tamaño, fecha
    imprime_entradas(entradas, total)
    guarda_entradas(entradas, total, arch_salida)
    guarda_entradas_csv(entradas, arch_salida_csv)
    guarda_entradas_json(entradas, total, arch_salida_json)
    guarda_entradas_json2(entradas, total, arch_salida_json2)

    
if __name__ == "__main__":  # el script es el programa principal?
    main()


