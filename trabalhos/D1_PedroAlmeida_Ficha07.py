# Exercício 1
# frase = input("Escreve uma frase: ")
# print(f"O comprimento da frase introduzida é igual a {len(frase)}")

# Exercício 2
# frase = input("Escreve uma frase: ")
# for i in range(len(frase)):
#     if frase[i] == " ":
#         print("_", end="")
#     else:
#         print(frase[i], end="")

# Exercício 3
# frase = input("Escreve uma frase: ")
# for i in range(len(frase)-1, -1, -1):
#     print(frase[i], end="")

# Exercício 4
# frase = input("Escreve uma frase: ")
# espacos = 0
# for i in range(len(frase)):
#     if frase[i] == " ":
#         espacos += 1
#
# print(f"A frase '{frase}' tem {espacos} espaços")

# Exercício 5 - segunda verificação FAZER
# frase = input("Escreve uma frase: ")
# if frase[len(frase)-1] == ".":
#     print(f"A frase '{frase}' termina com ponto final.")
# else:
#     print(f"A frase '{frase}' não termina com ponto final.")
# - SEGUNDA VERIFICAÇÃO -
# frase = input("Escreve uma frase: ")
# if frase.endsWith("."):
#     print(f"A frase '{frase}' termina com ponto final.")
# else:
#     print(f"A frase '{frase}' não termina com ponto final.")


# Exercício 6
# nome = input("Escreve um nome: ")
# if nome[len(nome)-1].lower() == "a":
#     print("Provavelmente é uma rapariga.")
# else:
#     print("Provavelmente é um rapaz.")

# Exercício 7
# frase = input("Escreve uma frase: ")
# ultimaLetra = frase[len(frase)-1]
# tipoFrase = ""
#
# if ultimaLetra == "!":
#     tipoFrase = "exclamativa"
# elif ultimaLetra == "?":
#     tipoFrase = "interrogativa"
# else:
#     tipoFrase = "afirmativa"
#
# print(f"A frase introduzida é {tipoFrase}.")

# Exercício 8
# frase = input("Escreve uma frase: ")
# ultimaLetra = frase[len(frase)-1]
# penultimaLetra = frase[len(frase)-2]
# tipoFrase = ""
#
# if ultimaLetra == "!":
#     if penultimaLetra == "?":
#         tipoFrase = "interrogativa exclamativa"
#     else:
#         tipoFrase = "exclamativa"
# elif ultimaLetra == "?":
#     if penultimaLetra == "!":
#         tipoFrase = "interrogativa exclamativa"
#     else:
#         tipoFrase = "interrogativa"
# else:
#     tipoFrase = "afirmativa"
#
# print(f"A frase introduzida é {tipoFrase}.")

# Exercício 9
# Numa linha do terminal, podem-se escrever 115 caracteres, independentemente do tamanho do terminal.
# ff = input()
# print(len(ff))

# Exercício 10
# frase = input("Escreve uma frase: ")
# espaco = " "
# for i in range(115-len(frase)):
#     espaco += " "
# print(espaco + frase)

# MINI PROJETO 2
import os
def clear():
    os.system("cls")
# Retirei este código da internet para poder limpar a consola

jogar = "s"
while jogar == "s":
    print("---- JOGO DA FORCA ----")

    palavra = input("Escolhe a palavra: ")
    if len(palavra) == 0:
        print("erro: A palavra não foi escolhida")
        break
    elif ("_" in palavra) or (" " in palavra):
        print("erro: A palavra não pode conter espaços ou underscores")
        break

    erros = input("Escolhe o número de tentativas erradas possível: ")
    if len(erros) == 0:
        print("erro: O número de tentativas erradas possíveis não foi escolhido")
        break
    elif int(erros) <= 0:
        print("erro: O número de tentativas erradas possíveis não pode ser menor ou igual a 0")
        break

    palavraAdivinhada = ""
    for i in range(len(palavra)):
        palavraAdivinhada += "_ "

    nErros = int(erros)
    contagemErros = 0

    clear()
    print(f"Palavra: {palavraAdivinhada}")
    while contagemErros < nErros:
        letra = input("\nQual é a letra da jogada? ")
        if len(letra) == 0:
            print("erro: Tens que escrever uma letra. Tenta outra vez")
            continue

        if not (letra in palavra):
            contagemErros += 1
        else:
            if letra in palavraAdivinhada:
                print("\nLetra repetida! Já tinhas adivinhado esta letra")
            else:
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        palavraAdivinhada = palavraAdivinhada[:i*2] + palavra[i] + palavraAdivinhada[i*2+1:]

        print(f"(Erros: {contagemErros}) Palavra: {palavraAdivinhada}")

        if not ("_" in palavraAdivinhada):
            print(f"\nPARABÉNS!\nAdivinhaste a palavra: {palavra.upper()}")
            break

    if contagemErros == nErros:
        print(f"\nGAME OVER!\nErraste {nErros} vezes!\nA palavra era: {palavra.upper()}")
        break

    jogar = input("\nQueres jogar outra vez? (S/N) ").lower()
