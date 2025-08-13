lista1 = [1,2]
lista2 = [3,4]

def somasdaslistas(lista1, lista2):
    for numerospai in lista2:
        lista1.append(numerospai)
    return lista1

print(somasdaslistas(lista1, lista2))