import forca
import adivinhacao


def escolhe_jogo():
    print("*"*33)
    print("*"*6, "Escolhe o seu jogo!", "*"*6)
    print("*"*33)

    print("(1) Forca (2) Advinhação (3) Sair")

    jogo = int(input("Qual Jogo? "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    else:
        exit()


if (__name__ == "__main__"):
    escolhe_jogo()
