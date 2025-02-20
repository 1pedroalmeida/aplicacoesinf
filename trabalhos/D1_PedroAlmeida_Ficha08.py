# Exercício 1
# a) Multiplicar um número n por 3
# b) triplo
# c) 1
# d) Devolver um valor sempre que a função é chamada
# e) def triplo(n):
# f)    t = 3 * n
#       return t
# g) 15
# h) erro

# Exerício 2
# def bom_dia():
#     print("Bom dia")
#
# bom_dia()

# Exercício 3
# def bom_dia():
#     print("Bom dia")
#
# def boa_tarde():
#     print("Boa tarde")
#
# def boa_noite():
#     print("Boa noite")
#
# hora = int(input("Qual é a hora atual? "))
#
# if hora > 24 or hora < 0:
#     print("erro: A hora não é válida")
# else:
#     if hora >= 6 and hora <= 12:
#         bom_dia()
#     elif hora > 12 and hora < 20:
#         boa_tarde()
#     else:
#         boa_noite()

# Exercício 4
# def boas_vindas(hora):
#     if hora > 24 or hora < 0:
#         print("erro: A hora não é válida")
#     else:
#         if hora >= 6 and hora <= 12:
#             print("Bom dia")
#         elif hora > 12 and hora < 20:
#             print("Boa tarde")
#         else:
#             print("Boa noite")
#
# hora = int(input("Qual é a hora atual? "))
# boas_vindas(hora)

# Exercício 5
# resultado esperado: 1/5/1 | A variável n dentro da função é apenas local, logo o valor não se altera fora da função
# def exemplo():
#     n = 5
#     print(n)
#
# n = 1
# print(n)
# exemplo()
# print(n)

# Exercício 6
# resultado esperado: 1/5/5 | Neste caso, a variável n dentro do corpo da função é global, logo o valor de n também se altera quando a função é chamada
# def exemplo():
#     global n
#     n = 5
#     print(n)
# n = 1
# print(n)
# exemplo()
# print(n)

# Exercício 7
# def dobro(num):
#     return num * 2

# Exercício 8
# def soma(num1, num2):
#     return num1 + num2
#
# print("| Somar dois números |")
# num1 = int(input("Primeiro número: "))
# num2 = int(input("Segundo número: "))
#
# print(f"\nResultado: {soma(num1, num2)}")

# Exercício 9
# def maior(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# Exercício 10
# def func():
#     for i in range(10):
#         print(i + 1)
#
# func()

# Exercício 11
# def listaNums(num):
#     for i in range(num):
#         print(i + 1)
#
# listaNums(14)

# Exercício 12

