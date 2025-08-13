recebidordalista = input("Digite uma lista de números separados por vírgula: ")
listanumeros = [int(numero) for numero in recebidordalista.split(",")]

def filtrarpares(listanumeros):
    listaimpar = [numero for numero in listanumeros if numero % 2 == 1]
    return listaimpar

print(filtrarpares(listanumeros))