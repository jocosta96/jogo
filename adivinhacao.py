def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha um nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    dificuldade = int(input("Selecione a dificuldade: "))

    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {} e você fez {} pontos ".format(numero_secreto, pontos))

            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {} e você fez {} pontos ".format(numero_secreto, pontos))

            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
