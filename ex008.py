listademerda = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def somar(listademerda):
    soma = 0
    for numero in listademerda:
        soma += numero
    return soma

# solução mais simples: return sum(listademerda)

print(somar(listademerda))