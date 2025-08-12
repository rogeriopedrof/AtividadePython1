recebalista = input("Digite uma lista de elementos separados por vírgula: ")
listareal = recebalista.split(",") #faz a separação da string em uma lista, nesse caso, separando por vírgula

for i in range(len(listareal)):
    print(listareal[i])