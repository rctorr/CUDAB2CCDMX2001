import click
import csv
import json
import os

@click.command()
@click.argument("nomarch")
def csvtojson(nomarch):
    """
    Lee el nombre de archivo proporcionado por el usuario en
    formato CSV y lo guarda en formato JSON con el mismo
    nombre, s´olo cambia la extensi´on.
    """
    nomjson = os.path.splitext(nomarch)[0] + ".json"
    
    # Leer el archivo csv
    with open(nomarch) as da:
        csv_reader = csv.reader(da)
        listajson = []
        encabezados = []
        for fila in csv_reader:
            if not encabezados:
                encabezados = fila
            else:
                filadict = {}
                for i,valor in enumerate(fila):
                    filadict[encabezados[i]] = valor
                # {"nomenc1": valor, "nomenc2": valor, ...}
                listajson.append(filadict)
                            
    # Guardar el archivo json
    with open(nomjson, "w") as da_json:
        json.dump(listajson, da_json, indent=4)

if __name__ == "__main__":
    csvtojson()