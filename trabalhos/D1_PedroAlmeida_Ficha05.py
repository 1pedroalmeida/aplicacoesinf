import turtle
import math

# Exercício 1
def quadrado(n):
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)

# Exercício 2
# -- programa 1 --
# for i in range(1, 11):
#     quadrado(15*i)
#
# -- programa 2 --
# for i in range(11, 1, -1):
#     quadrado(15*i)
#
# -- programa 3 --
# for i in range(10):
#     i+=1
#     quadrado(10*i)
#     turtle.penup()
#     turtle.forward((10*i) + 5)
#     turtle.pendown()
#
# -- programa 4 --
# for i in range(5, 0, -1):
#     distancia = 20*i
#     proxDistancia = 20*(i-1)
#     dif = distancia - proxDistancia
#
#     quadrado(distancia)
#     turtle.penup()
#     turtle.right(45)
#     turtle.forward((2 * ((dif/2) ** 2)) ** (1/2)) # teorema de pitagoras
#     turtle.left(45)
#     turtle.pendown()

# Exercício 3
# color = ("green", "red", "yellow", "blue", "violet", "gray")
#
# for i in range(5, 0, -1):
#     distancia = 20*i
#     proxDistancia = 20*(i-1)
#     dif = distancia - proxDistancia
#
#     turtle.fillcolor(color[i])
#
#     turtle.begin_fill()
#     quadrado(distancia)
#     turtle.end_fill()
#
#     turtle.penup()
#     turtle.right(45)
#     turtle.forward((2 * ((dif/2) ** 2)) ** (1/2)) # teorema de pitagoras
#     turtle.left(45)
#     turtle.pendown()

# Exercício 4
# def espiral(n):
#     i = 1
#
#     while i <= n:
#         quadrado(10*i)
#         turtle.right(270/(n-1))
#         i+=1
#
# espiral(10)

# Exercício 5
def triangulo(n):
    for i in range(3):
        turtle.forward(n)
        turtle.right(120)

# for i in range(6):
#    triangulo(100)
#    turtle.forward(100)
#    turtle.right(60)

# Exercício 6
# turtle.penup()
# turtle.fillcolor("black")
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
#
# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(180)
#
# turtle.fillcolor("white")
# turtle.begin_fill()
# triangulo(100)
# turtle.end_fill()
#
# turtle.right(100)
# turtle.forward(60)
# turtle.begin_fill()
# turtle.circle(15)
# turtle.end_fill()

# Exercício 7
def trianguloRetangulo(cateto1, cateto2):
    hipotenusa = math.sqrt((cateto1 * cateto1) + (cateto2 * cateto2))
    anguloCat1Hip = math.degrees(math.asin(cateto2 / hipotenusa))
    anguloCat2Hip = math.degrees(math.asin(cateto1 / hipotenusa))

    turtle.forward(cateto1)
    turtle.left(180 - anguloCat1Hip)
    turtle.forward(hipotenusa)
    turtle.left(180 - anguloCat2Hip)
    turtle.forward(cateto2)

# cateto1 = int(input("Medida do cateto 1: "))
# cateto2 = int(input("Medida do cateto 2: "))
# trianguloRetangulo(cateto1, cateto2)

# Exercício 8
def trianguloAcutangulo(base, lado):
    anguloBaseLado = math.degrees(math.acos((base / 2) / lado))
    anguloLadoLado = 180 - (anguloBaseLado * 2)

    turtle.forward(base)
    turtle.left(180 - anguloBaseLado)
    turtle.forward(lado)
    turtle.left(180 - anguloLadoLado)
    turtle.forward(lado)
    turtle.left(180 - anguloBaseLado)

# base = int(input("Medida da base: "))
# lado = int(input("Medida dos lados: "))
# if ((2 * lado) > base):
#     trianguloAcutangulo(base, lado)

# Exercício 9
# angulo = (360 - (90 * 3)) / 3
# for i in range(3):
#    trianguloRetangulo(100,30)
#    turtle.right(180 - angulo)
#
# Exercício 10
# for i in range(10):
#    trianguloAcutangulo(30,100)
#    turtle.right(360/10)
