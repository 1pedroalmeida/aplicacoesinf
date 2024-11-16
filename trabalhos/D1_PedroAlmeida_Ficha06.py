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
#     if (x == "1") | (x == "2"):
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
print("-- gerar uma chave do euromilhões --")

num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
while num2 == num1:
    num2 = random.randint(1, 50)
num3 = random.randint(1, 50)
while (num3 == num1) | (num3 == num2):
    num3 = random.randint(1, 50)
    


for i in range(5):
    
