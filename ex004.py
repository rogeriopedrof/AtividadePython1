recebidordalista = input("Digite uma lista de números separados por vírgula: ")
listanumeros = [int(numero) for numero in recebidordalista.split(",")]

def filtrarpares(listanumeros):
    listapar = [numero for numero in listanumeros if numero % 2 == 0] # Filtra números pares.
    return listapar # Se você quer que a função entregue um valor para ser usado fora dela

print(filtrarpares(listanumeros))  # Imprime a lista de números pares filtrados