listademerda = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

recebidorn = int(input("Digite um número: "))

def recebeumnumerolista(recebidorn, listademerda):
    if recebidorn in listademerda: # 'in' verifica se o número está na lista
        return True
    else:
        return False
    
print(recebeumnumerolista(recebidorn, listademerda))  # Imprime True se o número estiver na lista, caso contrário False