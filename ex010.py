import random


def escolher_numero() :
    numero_usuario = int(input("Digite um número entre 0 e 5: "))

    if numero_usuario < 0 or numero_usuario > 5 :
        print("Número inválido. Por favor, digite um número entre 0 e 5.")
        escolher_numero()
    else :
        numero_aleatorio = random.randint(0, 5)
        print("O número escolhido pelo programa é:", numero_aleatorio)
        print("O número escolhido por você é:", numero_usuario)

        if numero_usuario == numero_aleatorio :
            print("Você Ganhou!!!")
        else :
            print("Você perdeu. Tente novamente.")


escolher_numero()
