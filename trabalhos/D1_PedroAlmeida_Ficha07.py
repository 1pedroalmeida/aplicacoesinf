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

