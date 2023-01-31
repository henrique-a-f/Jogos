import forca
import advinhacao

print("*"*33)
print("*"*6, "Escolhe o seu jogo!", "*"*6)
print("*"*33)

print("(1) Forca (2) Advinhação (3) Sair")

jogo = int(input("Qual Jogo? "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Advinhação")
    advinhacao.jogar()
else:
    exit()
