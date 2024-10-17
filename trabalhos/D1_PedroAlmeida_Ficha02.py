# Exercício 1
print("bom dia!")

# Exercício 2
nome = input("Como te chamas? ")
print("Olá ", nome)

# Exercício 3
nome = input("Qual é o teu nome? ")
apelido = input("Qual é o teu apelido? ")
print("Olá", nome, apelido)

# Exercício 
# print("Quero somar dois números")
# a = int(input("Escreva o primeiro número: "))
# b = int(input("Escreva o segundo número: "))
# c = a+b
# print("A soma de ",a,"com ",b, "é ",c)

# Exercício 4
num = int(input("Introduz um número: "))
print("O número introduzido foi ",num)

# Exercício 5
num = int(input("Introduz um número: "))
print(num * 2)

# Exercício 6
num = int(input("Introduz um número: "))
print("O dobro é ",num*2)

# Exercício 7
num = int(input("Introduz um número: "))
print("O dobro de ",num, "é",num*2)

# Exercício 8
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print("Resultado: ",num1*num2)

# Exercício 9
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print("Divisão do primeiro pelo segundo: ",num1/num2)
print("Divisão do segundo pelo primeiro: ",num2/num1)

# Exercício 10
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print("Divisão do primeiro pelo segundo: ",num1//num2)
print("Divisão do segundo pelo primeiro: ",num2//num1)

# Exercício 11
num1= int(input("Introduz um número: "))
num2= int(input("Introduz outro número: "))
soma=num1+num2
subtracao=num1-num2
multiplicacao=num1*num2
divisao=num1/num2

print("\nResultados:\n","  Soma =",soma,"\n   Subtração =",subtracao,"\n   Multiplicação =",multiplicacao,"\n   Divisão =",divisao)

# Exercício 12
num1= int(input("Introduz um número: "))
num2= int(input("Introduz outro número: "))
divReal = num1/num2
divInt = num1//num2
divResto = divReal - divInt

print("\nDivisão (real) =",divReal, "\nDivisão (inteira) =",divInt,"\nDivisão (resto) =",divResto)

# Exercício 13
a = int(input("Primeiro valor? "))
b = int(input("Segundo valor? "))

tempa = a
tempb = b

print("a =",a,"\nb =",b)

a = tempb
b = tempa

print("\na =",a,"\nb =",b)

# Exercício 14
a = "string"
b = 1
c = True

print(type(a))  # str
print(type(b))  # int
print(type(c))  # bool
