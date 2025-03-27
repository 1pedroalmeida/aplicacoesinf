# Exercício 1
# texto, números, listas

# Exercício 2
# Acho que não

# Exercício 3
# strings, números inteiros, listas, tuplos, dicionários, sets e booleans

# Exercício 4
# Um array é uma coleção que nos permite guardar uma variedade de dados, de forma organizada

# Exerício 5
# Enquanto um vetor apenas nos permite armazenar informação em duas dimensões, uma tabela oferece-nos um número infinito de dimensões, assemelhando-se assim aos arrays.

# Exerício 6
# Sim, nomeadamente as listas, os tuplos, os dicionários e os sets.

# Exerício 7
# Em python, uma lista é uma coleção de dados sequenciada.

# Exercício 8
# a) 
# Vetor = [1, 5, 25, 123, 72]
# b) 
# Vetor[0] = 199
# c) 
# Vetor[len(Vetor)-1] = 250
# d) 
# valor = int(input("Novo valor (segunda posição): "))
# Vetor[1] = valor
# e) 
# print(Vetor[len(Vetor)-1])
# f)
# Vetor = [1,2,3,4,5,6,7,8,9,10]
# g)
# Vetor = [1.0,2.0,3.0,4.0]

# Exercício 9
# Os dados guardados numa lista são mutáveis (podem ser alterados), ao contrário do que acontece com os tuplos (são imutáveis).

# Exercício 10
# vetor = ( 1, 4, 7, 12, 9, 2, 5, 16, 99, 2 )
# for i in range(len(vetor)):
#     print(str(vetor[i]) + " ", end="")

# Exercício 11
# nums = []
# for i in range(5):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     nums.append(num)
#
# for i in range(5):
#     print(str(nums[i]) + ",", end="")

# Exerício 12
# nums = []
# for i in range(5):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     nums.append(num)
#
# for i in range(4, -1, -1):
#     print(str(nums[i]) + ",", end="")

# Exercício 13
# Executar o loop até ao penúltimo número e imprimir o último individualmente
# nums = []
# for i in range(5):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     nums.append(num)
#
# for i in range(4):
#     print(str(nums[i]) + ",", end="")
# print(nums[4])

# Exercício 14
# situação A - cria uma sequência de números de 0 até 5 (0, 1, 2, 3, 4)
# situação B - é uma coleção de dados organizada e imutável
# situação C - é uma coleção de dados organizada e mutável
# situação D - é uma coleção de dados desorganizada e que não permite repetições de valores

# Exercício 15
# numE = int(input("Introduz um número: "))
# nums = []
# for i in range(5):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     nums.append(num)
#
# for i in range(4):
#     print(str(nums[i]) + ",", end="")
# print(nums[4])
#
# if numE in nums:
#     print("O número existe no vetor.")
# else:
#     print("O número não existe no vetor.")

# Exercício 16
# import random
#
# num = int(input("Introduz um número de 1 a 20: "))
# nums = []
#
# for i in range(10):
#     nums.append(random.randint(1, 20))
#
# print("Os números gerados aleatoriamente foram:")
# for i in range(10):
#     print(str(nums[i]) + " ", end="")
#
# if num in nums:
#     print("\n\nO número escolhido encontra-se na lista de números gerados de forma aleatória.")
# else:
#     print("\n\nO número escolhido não se encontra na lista de números gerados de forma aleatória.")

# Exercício 17
# import random
#
# num = int(input("Introduz um número de 1 a 20: "))
# nums = []
#
# for i in range(10):
#     nums.append(random.randint(1, 20))
#
# print("Os números gerados aleatoriamente foram:")
# for i in range(10):
#     print(str(nums[i]) + " ", end="")
#
# if num in nums:
#     print(f"\n\nO número escolhido encontra-se na lista de números gerados de forma aleatória na posição {nums.index(num)+1}.")
# else:
#     print("\n\nO número escolhido não se encontra na lista de números gerados de forma aleatória.")

# Exercício 18
# import random
#
# num = int(input("Introduz um número de 1 a 20: "))
# nums = []
#
# for i in range(10):
#     nums.append(random.randint(1, 20))
#
# print("Os números gerados aleatoriamente foram:")
# for i in range(10):
#     print(str(nums[i]) + " ", end="")
#
# if num in nums:
#     cont = 0
#     pos = ""
#     for i in range(10):
#         if nums[i] == num:
#             cont += 1
#             pos += str(i+1) + ", "
#
#     print(f"\n\nO número escolhido aparece {cont} vez(es) na lista de números gerados de forma aleatória na(s) posição(ões) {pos[:-2]}.")
# else:
#     print("\n\nO número escolhido não se encontra na lista de números gerados de forma aleatória.")

# Exercício 19
# nums = []
# for i in range(10):
#     nums.append(int(input(f"Introduz o {i+1}º número: ")))
#
# soma = 0
# for i in range(10):
#     soma += nums[i]
#
# media = soma//10
# print("Média: " + media)

# Exercício 20
# nums = []
# for i in range(10):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     if num < 0:
#         num = 0
#     nums.append(num)
#
# soma = 0
# for i in range(10):
#     soma += nums[i]
#
# media = soma//10
# print("Média: " + media)

# Exercício 21
# import random
#
#
# def gerar(n):
#     Contagem = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
#
#     for i in range(n):
#         num = random.randint(1, 6)
#         Contagem[str(num)] += 1
#
#     return Contagem
#
#
# cont = gerar(1000)
# print("O programa gerou 1000 números aleatoriamente. Resultados: ")
#
# for i in range(6):
#     print(f"{i+1} - {cont[str(i+1)]} vezes")

# Exercício 22
# Meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
# print(f"Os meses que têm 30 dias são: {Meses[3]}, {Meses[5]}, {Meses[8]}, {Meses[10]}.")

# Exercício 23
# import random
#
#
# chave = {"numeros": [], "estrelas": []}
#
# for i in range(5):
#     num = random.randint(1, 50)
#     while num in chave["numeros"]:
#         num = random.randint(1, 50)
#
#     chave["numeros"].append(num)
#
# for i in range(2):
#     estrela = random.randint(1, 11)
#     while estrela in chave["estrelas"]:
#         estrela = random.randint(1, 11)
#
#     chave["estrelas"].append(estrela)
#
# print("A chave do euromilhões foi gerada com sucesso.")
#
# print("- Números:")
# for i in range(5):
#     print("  " + str(chave["numeros"][i]))
#
# print("- Estrelas:")
# for i in range(2):
#     print("  " + str(chave["estrelas"][i]))

# Exercício 24
# kg = [45, 51, 49, 64, 78, 59]
# soma = 0
#
# for i in range(len(kg)):
#     soma += kg[i]
#
# media = soma//len(kg)
#
# print(f"A soma de todos os elementos do vetor kg é {soma}")
# print(f"A média de kg dos valores registados no vetor é {media}")

# Exercício 25
# nums = []
#
# for i in range(10):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     nums.append(num)
#
# print("\nOs números introduzidos foram:")
# for i in range(10):
#     print("  " + str(nums[i]))
#
# soma = 0
# for i in range(10):
#     soma += nums[i]
#
# media = soma/10
#
# max = nums[0]
# min = nums[0]
#
# for i in range(10):
#     if nums[i] > max:
#         max = nums[i]
#     if nums[i] < min:
#         min = nums[i]
#
# print(f"\nSoma: {soma}")
# print(f"Média: {media}")
# print(f"Número máximo: {max}")
# print(f"Número mínimo: {min}")

# Exercício 26
# nums = []
#
# n = int(input("Define a quantidade de números a introduzir: "))
#
# for i in range(n):
#     num = int(input(f"Introduz o {i+1}º número: "))
#     nums.append(num)
#
# print("\nOs números introduzidos foram:")
# for i in range(n):
#     print("  " + str(nums[i]))
#
# soma = 0
# for i in range(n):
#     soma += nums[i]
#
# media = soma/n
#
# max = nums[0]
# min = nums[0]
#
# for i in range(n):
#     if nums[i] > max:
#         max = nums[i]
#     if nums[i] < min:
#         min = nums[i]
#
# print(f"\nSoma: {soma}")
# print(f"Média: {media}")
# print(f"Número máximo: {max}")
# print(f"Número mínimo: {min}")
