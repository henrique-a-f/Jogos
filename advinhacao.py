from random import randint

print("*"*32)
print("Bem Vindo ao jogo de Advinhação!")
print("*"*32)

numero_secreto = randint(0, 100)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! o seu número foi menor que o número secreto.")

print("O número secreto era: ", numero_secreto)
print("Fim do jogo")
