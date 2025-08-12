lista = [1, 2, 2, 3]
listasemrepetidos = list(set(lista)) #tira as repetições(set) e transforma em lista(list)
listasemrepetidos.sort() #ordena a lista

print(listasemrepetidos[-2]) #imprime o penúltimo elemento