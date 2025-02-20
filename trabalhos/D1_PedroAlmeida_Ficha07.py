import unicodedata

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
# import os
# def clear():
#     os.system("cls")
# Retirei este código da internet para poder limpar a consola
#
# jogar = "s"
# while jogar == "s":
#     print("---- JOGO DA FORCA ----")
#
#     palavra = input("Escolhe a palavra: ")
#     if len(palavra) == 0:
#         print("erro: A palavra não foi escolhida")
#         break
#     elif ("_" in palavra) or (" " in palavra):
#         print("erro: A palavra não pode conter espaços ou underscores")
#         break
#
#     erros = input("Escolhe o número de tentativas erradas possível: ")
#     if len(erros) == 0:
#         print("erro: O número de tentativas erradas possíveis não foi escolhido")
#         break
#     elif int(erros) <= 0:
#         print("erro: O número de tentativas erradas possíveis não pode ser menor ou igual a 0")
#         break
#
#     palavraAdivinhada = ""
#     for i in range(len(palavra)):
#         palavraAdivinhada += "_ "
#
#     nErros = int(erros)
#     contagemErros = 0
#
#     clear()
#     print(f"Palavra: {palavraAdivinhada}")
#     while contagemErros < nErros:
#         letra = input("\nQual é a letra da jogada? ")
#         if len(letra) == 0:
#             print("erro: Tens que escrever uma letra. Tenta outra vez")
#             continue
#
#         if not (letra in palavra):
#             contagemErros += 1
#         else:
#             if letra in palavraAdivinhada:
#                 print("\nLetra repetida! Já tinhas adivinhado esta letra")
#             else:
#                 for i in range(len(palavra)):
#                     if palavra[i] == letra:
#                         palavraAdivinhada = palavraAdivinhada[:i*2] + palavra[i] + palavraAdivinhada[i*2+1:]
#
#         print(f"(Erros: {contagemErros}) Palavra: {palavraAdivinhada}")
#
#         if not ("_" in palavraAdivinhada):
#             print(f"\nPARABÉNS!\nAdivinhaste a palavra: {palavra.upper()}")
#             break
#
#     if contagemErros == nErros:
#         print(f"\nGAME OVER!\nErraste {nErros} vezes!\nA palavra era: {palavra.upper()}")
#         break
#
#     jogar = input("\nQueres jogar outra vez? (S/N) ").lower()

# Exercício 11
# frase = input("Escreve uma frase: ")
# espaco = " "
# for i in range(round((115-len(frase))/2)):
#     espaco += " "
#
# print(espaco, frase, espaco)

# Exercício 12
# frase = input("Escreve uma frase: ")
# num = int(input("1 - Esquerda\n2 - Centro\n3 - Direita\n> "))
# espaco = " "
#
# if num == 1:
#     print(frase)
# elif num == 2:
#     for i in range(round((115-len(frase))/2)):
#         espaco += " "
#     print(espaco, frase, espaco)
# elif num == 3:
#     for i in range(115 - len(frase)):
#         espaco += " "
#     print(espaco + frase)

# Exercício 13
# frase = input("Escreve uma frase: ")
# letrasMaiusculas = 0
#
# for i in range(len(frase)):
#     if frase[i].isupper():
#         letrasMaiusculas += 1
#
# print(f"A frase tem {letrasMaiusculas} letras maiúsculas")

# Exercício 14
# frase = input("Escreve uma frase: ")
# letrasMaiusculas = 0
# letrasMinusculas = 0
#
# for i in range(len(frase)):
#     if frase[i].isupper():
#         letrasMaiusculas += 1
#     elif frase[i].islower():
#         letrasMinusculas += 1
#
# print(f"A frase tem {letrasMaiusculas} letras maiúsculas e {letrasMinusculas} letras minúsculas.")

# Exercício 15
# frase = input("Escreve uma frase: ")
# letrasMaiusculas = 0
# letrasMinusculas = 0
# algarismos = 0
# outros = 0
#
# for i in range(len(frase)):
#     if frase[i].isupper():
#         letrasMaiusculas += 1
#     elif frase[i].islower():
#         letrasMinusculas += 1
#     elif frase[i].isnumeric():
#         algarismos += 1
#     else:
#         outros += 1
#
# print(f"A frase tem:\n- {letrasMaiusculas} letras maiúsculas\n- {letrasMinusculas} letras minúsculas\n- {algarismos} algarismos\n- {outros} outros caracteres")

# Exercício 16
# palavra = input("Escreve uma palavra: ")
# novaPalavra = ""
#
# for i in range(len(palavra)-1, -1, -1):
#     novaPalavra += palavra[i]
#
# if novaPalavra == palavra:
#     print("A palavra introduzida é um palíndromo.")
# else:
#     print("A palavra introduzida não é um palíndromo.")

# Exercício 17
# frase = input("Escreve uma frase: ")
# print(f"\nFrase introduzida: {frase}\n  - Letras maiúsculas: {frase.upper()}\n  - Letras minúsculas: {frase.lower()}")

# Exercício 18
# frase = input("Escreve uma frase: ")
# novaFrase = ""
#
# for i in range(len(frase)):
#     if frase[i] != " ":
#         novaFrase += frase[i].lower()
#
# for i in range(len(novaFrase)-1, round(len(novaFrase)/2)-1, -1):
#     if(novaFrase[i] != novaFrase[len(novaFrase)-i-1]):
#         print("A frase introduzida não é um palíndroma.")
#         exit()
# print("A frase introduzida é um palíndroma.")

# Exercício 19
# frase = input("Escreve uma frase: ")
# novaFrase = ""
#
# for i in range(len(frase)):
#     if not (ord(frase[i]) < 48 and ord(frase[i]) > 31):
#         novaFrase += frase[i].lower()
#
# for i in range(len(novaFrase)-1, round(len(novaFrase)/2)-1, -1):
#     if(novaFrase[i] != novaFrase[len(novaFrase)-i-1]):
#         print("A frase introduzida não é um palíndroma.")
#         exit()
# print("A frase introduzida é um palíndroma.")

# Exercício 20
# frase = input("Escreve uma frase: ")
# frase = ''.join([c for c in unicodedata.normalize('NFKD', frase) if not unicodedata.combining(c)]) # Retirei este código da internet, porque não estava a conseguir transformar os as letras com acento em letras normais de forma simples
# novaFrase = ""
#
# for i in range(len(frase)):
#     if not (ord(frase[i]) < 48 and ord(frase[i]) > 31):
#         novaFrase += frase[i].lower()
#
# for i in range(len(novaFrase)-1, round(len(novaFrase)/2)-1, -1):
#     if(novaFrase[i] != novaFrase[len(novaFrase)-i-1]):
#         print("A frase introduzida não é um palíndroma.")
#         exit()
# print("A frase introduzida é um palíndroma.")

# Exercício 21
# primeiro = input("Qual é o teu primeiro nome? ")
# apelido = input("Qual é o teu último nome? ")
# nome = primeiro + " " + apelido

# Exercício 22
# nome = input("Qual é o teu primeiro nome? ") + " " + input("Qual é o teu último nome? ")

# Exercício 23
# frase = input("Escreve uma frase: ")
# letra = input("Escreve a letra que queres remover da frase: ")
#
# print(frase.replace(letra, ""))
