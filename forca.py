def jogar():
    print("*"*34)
    print("*"*3, "Bem Vindo ao jogo da Forca!", "*"*3)
    print("*"*34)

    palavra_secreta = "maçã".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                    # print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Não foi dessa vez. Você perdeu!")
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
