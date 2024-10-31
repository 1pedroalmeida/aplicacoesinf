import turtle

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
