from random import randint

print("*"*32)
print("Bem Vindo ao jogo de Advinhação!")
print("*"*32)

numero_secreto = randint(1, 100)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou: {:3d}".format(chute))

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! o seu número foi menor que o número secreto.")

print("O número secreto era: {:3d}".format(numero_secreto))
print("Fim do jogo")
