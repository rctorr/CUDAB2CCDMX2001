# Importación de módulos
import random

# Lee el valor de número de claves n
esCorrecto = False  # Bandera para el ciclo while
while not esCorrecto:
    n = input("Cuantas claves a generar n: ")
    esCorrecto = n.isdigit()
    if not esCorrecto:
        print("El valor ", n, " no es un entero, por favor ingresa un entero.")
    else:
        n = int(n)

# Lee el valor de la longitud de las claves
m = 8
esCorrecto = False  # Bandera para el ciclo while
while not esCorrecto:
    r = input("Ingresa longitud de claves (8) m: ")
    esCorrecto = r.isdigit() or r == ""
    if not esCorrecto:
        print("El valor ", m, " no es un entero, por favor ingresa un entero.")
    else:
        if r.isdigit():
            m = int(r)

# Generando clave
# Incluyendo los símbolos: #$%&/
# Incluye mayúculas
mayusculas = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
minusculas = mayusculas.lower()
digitos = "1234567890"
simbolos = "#$%&/()=?!"
alfabeto = mayusculas + minusculas + digitos + simbolos

# Generando n claves
for x in range(n):
    clave = random.choice(mayusculas)
    clave += random.choice(minusculas)
    clave += random.choice(digitos)
    clave += random.choice(simbolos)

    # Cuántas letras no falta?
    nl = m - 4  # nl = número de letras
    faltan = random.choices(alfabeto, k=nl)  # regresa una lista ["a", "z", "5", ...]
    faltan = "".join(faltan)  # convertimos lista -> str
    clave += faltan  # clave = clave + faltan
    clave = "".join(random.sample(clave, m))
    print(clave)
