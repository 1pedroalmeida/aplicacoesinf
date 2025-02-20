---
layout: default
---

# 10 de janeiro de 2025

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise/comentário sobre a aula](#análisecomentário-sobre-a-aula)

---

## Conteúdos dados na aula

### Funções (revisão)

#### return

A instrução `return`, dentro de uma função, permite indicar um valor que a função retornará quando for chamada.

```py
def somar(a, b):
    return a + b

print(somar(1, 2)) # Irá apresentar 3 na consola
```

Também é possível retornar vários valores numa função.

```py
def somaProduto(a, b):
    soma = a + b
    produto = a * b

    return soma, produto

print(somaProduto(1, 2)) # Irá apresentar a soma e o produto entre 1 e 2 na consola
```

#### global

Ao criar uma variável dentro de uma função, esta torna-se apenas local, ou seja, não afeta o resto do código fora do corpo da função.

```py
nome = "rui"

def func():
    nome = "jaime"
    print("olá " + nome) # olá jaime

print("olá " + nome) # olá rui
```

A instrução `global`, no entanto, permite criar variáveis globais dentro de uma função que afetam o exterior da mesma.

```py
nome = "rui"

def func():
    global nome
    nome = "jaime"

func()

print("olá " + nome) # olá jaime
```

#### Parâmetros com valores predefinidos

As funções, em Python, possibilitam também a predefinição de valores padrão para os parâmetros, caso estes não sejam especificados.

```py
def func(nome="rui"):
    print("olá " + nome)

func()        # olá rui
func("jaime") # olá jaime
```

## Trabalho realizado na aula

## Análise/comentário sobre a aula

Nesta aula, fizemos uma revisão da matéria relacionada com as [funções em Python](aula_outubro_30.md), introduzindo também novos conceitos e instruções.

#### Links relevantes:

- Informação adicional:
    - Instrução `global`: <https://docs.python.org/pt-br/dev/reference/simple_stmts.html#global>
    - Instrução `return`: <https://docs.python.org/pt-br/dev/reference/simple_stmts.html#return>
    - Parâmetros padrão numa função: <https://docs.python.org/pt-br/3/tutorial/controlflow.html#default-argument-values>
