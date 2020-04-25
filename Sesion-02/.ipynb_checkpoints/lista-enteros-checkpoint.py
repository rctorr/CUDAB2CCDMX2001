# Estilo de programación llamado
# MVC=Modelo Vista Controlador
n = 50000000

# Modelo: Obtener o generar datos o info.
# Crear lista de enteros
numeros = list(range(n))   # [1, 2, 3, ..., n]

# convertir lista a decimales
for i in range(n):  # i = 0, 1, 2, ..., n-1
    numeros[i] = float(numeros[i])

# Vista: Imprimir resultados, reportes, gráficas, archivos
# Se imprime la lista
for n in numeros:
    print(n)