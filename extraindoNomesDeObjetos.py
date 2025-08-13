objetos = [
    {"nome": "Rogério"},
    {"nome": "Eloi"},
    {"nome": "Guilherme"},
    {"nome": "Renato"},
    {"nome": "Francês"}
]

def pegar_nomes(objetos):
    return [objeto["nome"] for objeto in objetos] # Extrair nomes do dicionário
print(pegar_nomes(objetos))