def rango(n):
    i=0
    while i<n:
        yield i
        i += 1

for i in rango(10000000000000000000000000000000000000000):
    print(i)
