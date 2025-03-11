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
# def func(num1, num2):
#     if num1 > num2:
#         temp = num1
#         num1 = num2
#         num2 = temp
#     num1 += 1
#     while num1 < num2:
#         print(num1)
#         num1 += 1
#
# func(7, 1)

# Exercício 13
# def media(nota1, nota2):
#     return ((nota1 + nota2) / 2)

# Exercício 14
# def media(nota1, nota2):
#     if nota1 < 0 or nota1 > 20 or nota2 < 0 or nota2 > 20:
#         return -1
#     else:
#         return ((nota1 + nota2) / 2)

# Exercício 15
# def func(nota1, nota2, nota3):
#     if nota1 < 0 or nota1 > 20 or nota2 < 0 or nota2 > 20 or nota3 < 0 or nota3 > 20:
#         return -1
#     else:
#         media = (nota1 + nota2 + nota3) / 3
#         return (media >= 10)

# Exercício 16
# def tabuada(num):
#     for i in range(10):
#         print(num * (i+1))

# Exercício 17
# def primo(num):
#     for i in range(num-1, 0, -1):
#         if i == 1:
#             return True
#         if (num % i) == 0:
#             return False
#     return False

# Exercício 18
# def u(n):
#     if n > 0:
#         return (n + 1) / n

# Exercício 19
# A função devolve dois valores ao mesmo tempo, os números anterior e seguinte. De seguida, ambos os valores são atribuídos de uma só vez a duas variáveis que depois são apresentadas na consola

# Exercício 20
# def func(num):
#     return num/2, num*2

# Exercício 21
# def func(c, l):
#     return c*l, c*2 + l*2

# Exercício 22:
# def func(num1, num2):
#     return num1%num2, num1//num2, num1/num2

# Exercício 23
# def ascii(c):
#     return ord(c)

# Exercício 24
# def maiuscula(letra):
#     if not ((type(letra) == str) and len(letra) == 1):
#         return "*"
#     return letra.upper()

# Exercício 25
# def minuscula(letra):
#     if not ((type(letra) == str) and len(letra) == 1):
#         return "*"
#     return letra.lower()

# Exercício 26
# def func(c):
#     x = ord(c)
#     if x > 47 and x < 58:
#         return 1
#     elif x > 96 and x < 123:
#         return 2
#     elif x > 64 and x < 91:
#         return 3
#     else:
#         return 4

# Exercício 27
# Eu sou de França
# Eu sou de Portugal
# Eu sou de Brasil
# Eu sou de Canadá
# Não dará origem a erros, visto que a função nacionalidade tem um valor predefinido para o parâmetro pais

# Exercício 28
# def asteriscos(n):
#     for i in range(n):
#         print("*", end="")

# Exercício 29
# def asteriscos(n, ch = "*"):
#     for i in range(n):
#         print(ch, end="")

# Exercício 30
# def asteriscos_vertical(n):
#     for i in range(n):
#         print("*")

# Exercício 31
# def caracteres(n, ch):
#     for i in range(n):
#         print(ch, end="")

# Exercício 32
# def margem(n):
#     if n > 0:
#         print("*", end="")
#         for i in range(n):
#             print(" ", end="")
#         print("*")

# Exercício 33
# dim = int(input("Dimensão? "))
# for i in range(dim):
#     asteriscos(dim)
#     print("\n", end="")

# Exercício 34
# dim = int(input("Dimensão? "))
#
# b = dim  # base
# if dim % 2 == 0:
#     b = dim + 1
#
# h = (b+1) // 2  # altura
#
# for i in range(h):
#     m = ((b-1) // 2) - i
#     for i in range(m):
#         print(" ", end="")
#
#     asteriscos(b-(m*2))
#     print("\n", end="")

# Exercício 35
# def classificacao(nota):
#     if nota < 0 or nota > 20:
#         return None
#     elif nota <= 9.4:
#         return "Insuficiente"
#     elif nota <= 13.4:
#         return "Suficiente"
#     elif nota <= 17.4:
#         return "Bom"
#     else:
#         return "Muito Bom"

# Exercício 36
# def imc(massa, altura):
#     resultado = massa / (altura * altura)
#
#     if resultado < 16:
#         return "Magreza grave"
#     elif resultado < 17:
#         return "Magreza moderada"
#     elif resultado < 18.5:
#         return "Magreza leve"
#     elif resultado < 25:
#         return "Saudável"
#     elif resultado < 30:
#         return "Sobrepeso"
#     elif resultado < 35:
#         return "Obesidade Grau I"
#     elif resultado < 40:
#         return "Obesidade Grau II (severa)"
#     else:
#         return "Obesidade Grau III (mórbida)"

# Exercício 37
# def juntar(str1, str2):
#     return str1 + str2

# Exercício 38
# def func(frase):
#     return frase.split(" ")[0]

# Exercício 39
# def func(frase):
#     return frase.split(" ")[-1]

# Exerício 40
# def func(frase):
#     return len(frase.split(" "))
