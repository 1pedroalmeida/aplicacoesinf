import turtle

# Exercício 1
# turtle.forward(100)

# Exercício 2
# turtle.right(90)
# turtle.forward(100)

# Exercício 3
# for i in range(4):
#     turtle.forward(50)
#     turtle.right(90)

# Exercício 4
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)

# Exercício 5
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(120)

# Exercício 6
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# Exercício 7
# turtle.circle(200)

# Exercício 8
# for i in range(4):
#     turtle.circle(20)
#     turtle.penup()
#     turtle.forward(40)
#     turtle.pendown()

# Exercício 9
# for i in range(4):
#     if i == 0:
#         turtle.fillcolor("blue")
#     elif i == 1:
#         turtle.fillcolor("yellow")
#     elif i == 2:
#         turtle.fillcolor("pink")
#     else:
#         turtle.fillcolor("red")
#
#     turtle.begin_fill()
#     turtle.circle(30)
#     turtle.end_fill()
#
#     turtle.penup()
#     turtle.forward(60)
#     turtle.pendown()

# Exercício 10
# for i in range(5):
#     turtle.forward(100)
#     turtle.left(72)

# Exercício 11
# num_lados = int(input("Criar um polígono com o número de lados indicado: "))
#
# for i in range(num_lados):
#     turtle.forward(100)
#     turtle.left(360/num_lados)

# Exercício 12
# for i in range(20):
#     for i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
#     turtle.left(18)

# Exercício 13
# O exemplo apresentado começa por levantar a caneta de modo a não desenhar o percurso da tartaruga.
# De seguida é iniciado um ciclo for que cicla desde 40 até 0, sutraindo 1 valor à variavel a de cada vez.
# De cada vez que o código do ciclo é executado, a função turtle.stamp() deixa a marca do lugar da tartaruga, em seguida a instrução turtle.left(a) roda no sentido anti-horário o ângulo definido pelo valor da variável a e, por fim, turtle.forward(20) move a tartaruga 20 píxeis para a frente.
# Dado que o valor de a diminui cada vez que o ciclo é executado, também o ângulo de rotação para a esquerda vai diminuindo até ser nulo.
# O exemplo cria, portanto, uma espiral que se vai aproximando de uma linha reta ao longo do tempo.
#
#
# turtle.penup()
# for a in range(40, -1, -1):
#     turtle.stamp()
#     turtle.left(a)
#     turtle.forward(20)
