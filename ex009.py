listademerda = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

recebidorn = int(input("Digite um número: "))

def numeronalista(recebidorn, listademerda):
    return listademerda.count(recebidorn) # retorna quantas vezes o item aparece na lista

print(numeronalista(recebidorn, listademerda))