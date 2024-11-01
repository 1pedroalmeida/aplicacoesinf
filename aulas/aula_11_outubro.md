---
layout: default
---

# 11 de outubro de 2024

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise/comentário sobre a aula](#análisecomentário-sobre-a-aula)

---

## Conteúdos dados na aula

### Ciclos

#### O que são ciclos?

Ciclos são processoes únicos que nos permitem executar outras instruções repetidamente de forma eficiente.

Em python, existem dois tipos de ciclos, `while` e `for`.

#### While

O ciclo `while` executa um determinado conjunto de instruções, até que a condição especificada não se verifique.

```python
i = 10

# Neste caso, o corpo do ciclo irá ser executado até que a variável i seja menor que 1
while i >= 1:
    print(i)
    i-=1
```

#### For

Em contraste com o ciclo `while`, o ciclo `for` já não executa o código indefinidamente, até que uma condição pare de se verificar.

Neste caso, o ciclo itera apenas sobre uma sequência, até que esta chegue ao fim.

A função [`range`](https://docs.python.org/2/library/functions.html#range) está muitas vezes associada com o uso deste tipo de ciclo, de forma a criar sequências de números.

```python
# O corpo do ciclo irá ser executado para cada número de 10 até 1
for i in range(10, 0, -1):
    print(i)
```

## Trabalho realizado na aula

Continuação da realização da [ficha 3](../trabalhos/D1_PedroAlmeida_Ficha03.py)

## Análise/comentário sobre a aula
