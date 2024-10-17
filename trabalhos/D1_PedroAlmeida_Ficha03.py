# Exercício 1
num1 = int(input("Introduz um número: "))
num2 = int(input("Introduz outro número: "))

if num1 == num2:
    print("Os números introduzidos são iguais.")

# Exercício 2
num1 = int(input("Introduz um número: "))
num2 = int(input("Introduz outro número: "))

if num1 == num2:
    print("Os números introduzidos são iguais.")
else:
    print("Os números introduzidos são diferentes.")

# Exercício 3
num = int(input("Introduz um número: "))

if num > 0:
    print("O número introduzido é positivo.")
elif num < 0:
    print("O número introduzido é negativo.")
elif num == 0:
    print("O número introduzido é nulo.")

# Exercício 4
temperatura = int(input("Qual é a temperatura da água (graus C)? "))
estado = "líquido"

if temperatura > 100:
    estado = "gasoso"
elif temperatura < 0:
    estado = "sólido"

print("A água está no estado ", estado)

# Exercício 5
num1 = int(input("Introduz um número: "))
num2 = int(input("Introduz outro número: "))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print(num1)

# Exercício 6
num = int(input("Introduz um número: "))

if (num % 2) > 0:
    print("O número introduzido é ímpar")
else:
    print("O número introduzido é par")

# Exercício 7
num = int(input("Introduz um número: "))
if (num % 2) > 0:
    print("O número introduzido é ímpar")
else:
    print("O número introduzido é par")

num = int(input("Introduz um número: "))
if (num % 2) > 0:
    print("O número introduzido é ímpar")
else:
    print("O número introduzido é par")
    
# Exercício 8
i = 1
while i <= 9:
    print(i)
    i+=1
    
# Exercício 9
numFinal = int(input("Introduz um número final: "))
i = 1;

while i <= numFinal:
    print(i)
    i+=1
    
# Exercício 10
numFinal = int(input("Introduz um número final: "))
i = 1

while numFinal >= i:
    print(numFinal)
    numFinal-=1

# Exercício 11
num1 = int(input("Introduz o número inicial (menor): "))
num2 = int(input("Introduz o número final (maior): "))

while num1 <= num2:
    print(num1)
    num1+=1

# Exercício 12
num1 = int(input("Introduz o número inicial (maior): "))
num2 = int(input("Introduz o número final (menor): "))

while num1 >= num2:
    print(num1)
    num1-=1

# Exercício 13
num1 = int(input("Introduz o número inicial (menor): "))
num2 = int(input("Introduz o número final (maior): "))

while num1 <= num2:
    print(num1)
    num1+=2

# Exercício 14
num1 = int(input("Introduz o número inicial (maior): "))
num2 = int(input("Introduz o número final (menor): "))

while num1 >= num2:
    print(num1)
    num1-=5

# Exercício 15
num = int(input("Introduz um número: "))
i = 1

while i <=10:
    print(str(num) + "x" + str(i) + "=" + str(num * i))
    i+=1

# Exercício 16
num = int(input("Introduz um número: "))
inicial = int(input("Introduz um número inicial: "))
final = int(input("Introduz um número final: "))

while inicial <= final:
    print(str(num) + "x" + str(inicial) + "=" + str(num * inicial))
    inicial+=1

# Exercício 17
num1 = int(input("Introduz o número inicial: "))
num2 = int(input("Introduz o número final: "))

if num1%2 > 0:
    num1 +=1

while num1 <= num2:
    print(num1)
    num1 +=2

# Exercício 18
num1 = int(input("Introduz o número inicial: "))
num2 = int(input("Introduz o número final: "))

num1temp = num1

if num1temp%2 > 0:
    num1temp +=1

numerosPares = 0

while num1temp <= num2:
    numerosPares +=1
    num1temp +=2

print("Entre " + str(num1) + " e " + str(num2) + " há " + str(numerosPares) + " números pares.")

# Exercício 19
num1 = int(input("Introduz o número inicial: "))
num2 = int(input("Introduz o número final: "))

num1temp = num1
numerosPares = 0
numerosImpares = 0

while num1temp <= num2:
    if num1temp%2 > 0:
        numerosImpares +=1
    else:
        numerosPares +=1

    num1temp +=1

print("Entre " + str(num1) + " e " + str(num2) + " há " + str(numerosPares) + " números pares e " + str(numerosImpares) + " números ímpares.")

# Exercício 20
while True:
    num = int(input("Introduz um número: "))

    if num == 0:
        break
    elif num%2 > 0:
        print(str(num) + " é ímpar")
    else:
        print(str(num) + " é par")

# Exercício 21
num = int(input("Introduz um número: "))
x = num

if num == 1 or num == 0:
    print("O número introduzido não é primo.")
else:
    while x >= 1:
        if x == 1:
            print("O número introduzido é primo.")
            break
        elif x == num or num%x > 0:
            x-=1
            continue
        else:
            print("O número introduzido não é primo.")
            break

# Exercício 22
num1 = int(input("Introduz um número inicial: "))
num2 = int(input("Introduz um número final: "))

par = 0
impar = 0
primos = 0

if num1 > num2:
    a = num1
    b = num2
else:
    a = num2
    b = num1

while a >= b:
    if a%2 > 0:
        impar+=1
    else:
        par+=1

    # primos
    if a != 1 and a != 0:
        tempA = a-1
        while tempA >=1:
            if tempA == 1:
                primos+=1
                break
            elif a%tempA > 0:
                tempA-=1
                continue
            else:
                break
    a-=1

print("\nEntre", num1, "e", num2, "há:")
print("- números pares:", par)
print("- números ímpares:", impar)
print("- números primos:", primos)
