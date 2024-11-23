import random

# Exercício 1

# Exercício 2
# print(random.randint(0, 6))

# Exercício 3
# print("O dado foi lançado e saiu o número:", random.randint(0, 6));

# Exercício 4
# x = input("Lançar dado (S/N)?")
#
# while x.lower() != "n":
#     if x.lower() == "s":
#         print(random.randint(0, 6))
#         x = input("Lançar dado (S/N)?")
#     else:
#         break
#
# print("Terminado")

# Exercício 5
# x = input("Quantos dados (1, 2, s - sair)?")
#
# while x != "s":
#     if (x == "1") or (x == "2"):
#         if x == "2":
#             print(random.randint(0, 6))
#
#         print(random.randint(0, 6))
#         x = input("Quantos dados (1, 2, s - sair)?")
#     else:
#         break
#
# print("Terminado")

# Exercício 6
# Depois de executar várias vezes o seguinte programa, apercebi-me de que a função randrange não inclui o último elemento.
# A função randrange, assim como a função range, também aceita um valor que irá incrementar a sequência numérica.
# print(random.randint(1, 6))
# print(random.randrange(1, 6))

# Exercício 7
# print("-- gerar uma chave do euromilhões --")
#
# print("Números:")
# nums = []
# for i in range(5):
#     num = random.randint(1, 50)
#     for x in nums:
#         while x == num:
#             num = random.randint(1, 50)
#
#     nums.append(num)
#     print(" ", num)
#
# estrela1 = random.randint(1, 11)
# estrela2 = random.randint(1, 11)
# while estrela2 == estrela1:
#     estrela2 = random.randint(1, 11)
#
# print("Estrelas:")
# print(" ", estrela1)
# print(" ", estrela2)

# Exercício 8
# print("JOGO DO NÚMERO OCULTO")
# print("O objetivo do jogo é adivinhar um número desconhecido entre 1 e 10.\n")
# numCerto = random.randint(1, 10)
#
# num = int(input("Escreve um número: "))
# while num != numCerto:
#     num = int(input("O número está errado. Escreve outro número: "))
# if num == numCerto:
#     print("\nPARABÉNS!! Acertaste no número!")

# Exercício 9
# print("JOGO DO NÚMERO OCULTO")
# print("O objetivo do jogo é adivinhar um número desconhecido entre 1 e 10 em 3 tentativas.\n")
# numCerto = random.randint(1, 10)
# tentativas = 3
#
# num = int(input("Escreve um número (" + str(tentativas) + " tentativas): "))
# while (num != numCerto) and (tentativas != 1):
#     num = int(input("Errado. Escreve outro número (" + str(tentativas-1) + " tentativas): "))
#     tentativas -= 1
#
# if tentativas == 1:
#     print("\nQue pena! Não foi desta. Tenta outra vez!")
# else:
#     print("\nPARABÉNS!! Acertaste no número!")

# Exercício 10
# print("JOGO DO NÚMERO OCULTO")
# print("O objetivo do jogo é adivinhar um número desconhecido.\n")
#
# print("-> Configurar a dificuldade")
# intervalo = int(input("Escolher o intervalo de números\n  1-Fácil (1-5)\n  2-Médio (1-11)\n  3-Difícil (1-25)"))
# tentativas = int(input("Escolher o número de tentativas\n  1-Fácil (10)\n  2-Médio (5)\n  3-Difícil (3)"))
#
# if (intervalo > 3) or (intervalo < 1):
#     intervalo == 0
# if (tentativas > 3) or (tentativas < 1):
#     tentativas == 0
#
# if tentativas == 1:
#     tentativas = 10
# elif tentativas == 2:
#     tentativas = 5
#
# if intervalo == 1:  # fácil
#     numCerto = random.randint(1, 5)
# elif intervalo == 2:
#     numCerto = random.randint(1, 11)
# elif intervalo == 3:
#     numCerto = random.randint(1, 25)
#
# print("\n-> A DIFICULDADE FOI CONFIGURADA")
# while tentativas != 0:
#     num = int(input(f"({str(tentativas)} tentativas restantes)> "))
#     if num == numCerto:
#         break
#     tentativas -= 1
#
# if num == numCerto:
#     print("PARABÉNS!! Acertaste no número!")
# else:
#     print("Que pena! Não foi desta. Tenta outra vez!")

# Exercício 11
# print("JOGO DO NÚMERO OCULTO")
# print("O objetivo do jogo é adivinhar um número desconhecido.\n")
#
# print("-> Configurar a dificuldade")
# intervalo = int(input("Escolher o intervalo de números\n  1-Fácil (1-5)\n  2-Médio (1-10)\n  3-Difícil (1-25)"))
# tentativas = int(input("Escolher o número de tentativas\n  1-Fácil (10)\n  2-Médio (5)\n  3-Difícil (3)"))
#
# if (intervalo > 3) or (intervalo < 1) or (tentativas > 3) or (tentativas < 1):
#     print("\nConfiguração inválida")
#     exit()
#
# if tentativas == 1:
#     tentativas = 10
# elif tentativas == 2:
#     tentativas = 5
#
# if intervalo == 1:  # fácil
#     intervalo = 5
# elif intervalo == 2:  # médio
#     intervalo = 10
# elif intervalo == 3:  # difícil
#     intervalo = 25
#
# numTentativas = tentativas
# numCerto = random.randint(1, intervalo)
#
# print("\n-> A DIFICULDADE FOI CONFIGURADA")
# while tentativas != 0:
#     num = int(input(f"({str(tentativas)} tentativas restantes)> "))
#     if (num < 1) or (num > intervalo):
#         print("O número introduzido é inválido! Deve estar entre 1 e 10.")
#     if num == numCerto:
#         break
#     tentativas -= 1
#
# if num == numCerto:
#     print(f"PARABÉNS!! Acertaste no número em {str(numTentativas - tentativas + 1)} tentativas!")
# else:
#     print("Que pena! Não foi desta. Tenta outra vez!")

# Exercício 12
# print("Qual a dimensão do tabuleiro de jogo?")
# dimensaoX = int(input(" Dimensão horizontal = "))
# dimensaoY = int(input(" Dimensão vertifcal  = "))
#
# if (dimensaoX < 1) or (dimensaoY < 1):
#     print("Dimensões inválidas!")
#     exit()
#
# x = random.randint(1, dimensaoX)
# y = random.randint(1, dimensaoY)
#
# tentativa = 1
#
#
# def adivinhar(tentativa):
#     print()
#     xAdivinhado = int(input(f"X para a tentativa #{tentativa}: "))
#     yAdivinhado = int(input(f"Y para a tentativa #{tentativa}: "))
#
#     xDif = x - xAdivinhado
#     yDif = y - yAdivinhado
#
#     xAjuda = ""
#     yAjuda = ""
#
#     if xDif > 0:
#         xAjuda = "Oeste"
#     elif xDif < 0:
#         xAjuda = "Este"
#
#     if yDif > 0:
#         yAjuda = "Sul"
#     elif yDif < 0:
#         yAjuda = "Norte"
#
#     if (xAjuda == "") and (yAjuda == ""):
#         print(f"\nPARABÉNS!!! Acertaste em cheio à {tentativa}ª tentativa.")
#         exit()
#
#     if (xAjuda != "") and (yAjuda != ""):
#         xAjuda += ", "
#
#     print(f"Água! Tenta para {xAjuda}{yAjuda}")
#
#     tentativa += 1
#     adivinhar(tentativa)
#
# adivinhar(tentativa)

# Exercício 13
# Devemos adicionar outra coordenada, Z.


# Exercício 14
def jogo():
    print("-- PEDRA, PAPEL OU TESOURA --")

    numJogadas = int(input("Escolhe o número de jogadas da partida: "))
    if numJogadas < 1:
        print("\nNúmero de jogadas inválido!")
        exit()

    vitoriasJogador = 0
    vitoriasComputador = 0
    empates = 0

    while numJogadas != 0:
        jogadaComputador = random.randint(1, 3)
        jogadaJogador = input("A - Pedra\nB - Papel\nC - Tesoura").lower()

        if (jogadaJogador != "a") and (jogadaJogador != "b") and (jogadaJogador != "c"):
            print("\nJogada inválida! A jogada escolhida precisa de ser A, B ou C!")
            exit()

        if jogadaJogador == "a":
            jogadaJogador = 1
        elif jogadaJogador == "b":
            jogadaJogador = 2
        elif jogadaJogador == "c":
            jogadaJogador = 3

        if jogadaComputador == 1:
            jogadaComputador2 = "pedra"
        elif jogadaComputador == 2:
            jogadaComputador2 = "papel"
        else:
            jogadaComputador2 = "tesoura"

        # 1 > 3, pedra > tesoura 1 - 3 = -2
        # 2 > 1, papel > pedra   2 - 1 = 1
        # 3 > 2, tesoura > papel 3 - 2 = 1
        dif = jogadaJogador - jogadaComputador
        if jogadaJogador == jogadaComputador:
            empates += 1
            print(f"-> O computador também jogou {jogadaComputador2}. Empate!")
        elif (dif == -2) or (dif == 1):
            vitoriasJogador += 1
            print(f"-> O computador jogou {jogadaComputador2} e perdeu. Vitória!")
        else:
            vitoriasComputador += 1
            print(f"-> O computador jogou {jogadaComputador2} e ganhou. Fica para a próxima!")

        numJogadas -= 1

    print("\nO JOGO ACABOU!")
    print(f" Vitórias: {vitoriasJogador}\n Derrotas: {vitoriasComputador}\n Empates: {empates}")

    repetir = input("\nQueres jogar outra vez (S/N)? ").lower()
    if (repetir == "s"):
        print("\n")
        jogo()

jogo()
