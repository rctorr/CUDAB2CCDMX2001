import click
import csv
import json
import os
import time

## Modelo-Vista-Controlador (MVC)

## Modelo: obtiene datos
class Carpeta():
    def __init__(self, ruta):
        """ Constructor de la clase Carpeta """
        # Definiendo los atributos de la clase Carpeta
        self.ruta = ruta
        self.entradas = []
        self.total = 0
    
    def obtiene_entradas(self):
        """
        Obtiene la lista de entradas y regresa una lista
        con el nombre, tamaño y fecha.
        """
        # Se obtiene el nombre de las entradas
        nombres = os.listdir(self.ruta)
        # Ordenar alfab´eticamente
        nombres.sort(key=lambda nom: nom.lower())
        # Agregar la ruta a los nombres
        nombres = [os.path.join(self.ruta, n) for n in nombres]

        for n in nombres:
            fecha = os.path.getmtime(n)  # segundos
            fecha = time.ctime(fecha)  # str
            if os.path.isfile(n):  # path o ruta
                # -obtener el tamaño de n-
                # -agregarlo a la lista-
                tamanio = os.path.getsize(n)
                entrada = [n, tamanio, fecha]
                self.entradas.append(entrada)
                self.total += tamanio  # total = toal + tamanio
            else:
                # Entonces es un carpeta
                # -asignar tamaño igual cero-
                # -agregarlo a la lista-
                entrada = [n, 0, fecha]
                self.entradas.append(entrada)
                # total += 0  # si es cero, no tiene caso

        # Ordenando por tamaño de archivo
        self.entradas.sort(key=lambda elem: elem[1], reverse=True)

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
    """
    [
        ["nom1", 134, "fech1"],
        ["nom1", 134, "fech1"],
        ["nom1", 134, "fech1"],
    ]
    
    [
        {"nombre":"nom1", "tamanio":134, "fecha":"fech1"},
        {"nombre":"nom1", "tamanio":134, "fecha":"fech1"},
        {"nombre":"nom1", "tamanio":134, "fecha":"fech1"},
    ]    
    """
    #for i,e in enumerate(entradas):   # (1, e[0]), (2, e[1])
    #    entradas[i] = {"nombre": e[0], "tamanio":e[1], "fecha": e[2]}
    entradas = [
        {"nombre": e[0], "tamanio":e[1], "fecha": e[2]}
        for e in entradas
    ]
        
    with open(arch_salida_json, "w", encoding="utf-8") as da:
        json.dump(entradas, da, indent=4)

@click.command()
@click.argument("ruta", default=".")
def lc(ruta):
    """
    Lista los elementos de la carpeta ruta en la salida
    estandar.
    """
    arch_salida = "salida.txt"
    arch_salida_csv = "salida.csv"
    arch_salida_json = "salida.json"
    arch_salida_json2 = "salida2.json"

    # Obtener la lista de entradas
    carpeta = Carpeta(ruta)
    carpeta.obtiene_entradas()
    imprime_entradas(carpeta.entradas, carpeta.total)
    guarda_entradas(carpeta.entradas, carpeta.total, arch_salida)
    guarda_entradas_csv(carpeta.entradas, arch_salida_csv)
    guarda_entradas_json(carpeta.entradas, carpeta.total, arch_salida_json)
    guarda_entradas_json2(carpeta.entradas, carpeta.total, arch_salida_json2)
    
if __name__ == "__main__":
    lc()


