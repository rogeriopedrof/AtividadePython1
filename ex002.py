recebidordalista = input("Digite uma lista de números separados por vírgula: ")
listanumeros = [int(numero) for numero in recebidordalista.split(",")] # Converte a string em uma lista de inteiros. Papo de maluco-genio!

print('Seu maior número:', max(listanumeros))