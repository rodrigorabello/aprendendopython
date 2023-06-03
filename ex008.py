import random
def sortear_ordem():
    nomes = []
    for i in range(1, 5):
        nome = input(f'Digite o nome da pessoa {i}: ')
        nomes.append(nome)
    random.shuffle(nomes)
    return nomes
print(sortear_ordem())