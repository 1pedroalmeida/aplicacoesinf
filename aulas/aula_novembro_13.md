---
layout: default
---

# 13 de novembro de 2024

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise/comentário sobre a aula](#análisecomentário-sobre-a-aula)

---

## Conteúdos dados na aula

### Números aleatórios (pseudoaleatórios)

Em python, podemos gerar números aleatórios (incertos e que não seguem um padrão) através do uso de funções do módulo `random`.

No entanto, estes números são, na realidade, pseudoaleatórios, dado que são gerados atráves de algoritmos e fórmulas matemáticas que apenas se aproximam de um acontecimento verdadeiramente aleatório.

#### Random

##### randint

A função `randint` permite-nos gerar um número aleatório entre os valores fornecidos.

```python
# Importar o módulo
import random

# A variável num vai conter um número gerado aleatoriamente de 1 a 6
num = random.randint(1, 6)
```

##### randrange

Podemos usar também a função `randrange`, parecida com a função `range` (referida na [aula de 11 de outubro](aula_outubro_11.md#for)), que escolhe um número entre a série de números indicada, aleatoriamente.

```python
import random

# A variável num vai conter um número gerado aleatoriamente de 1 a 6, não incluindo o 6
num = random.randrange(6, 1, -1)
```

## Trabalho realizado na aula

Início da realização da [ficha 6](../trabalhos/D1_PedroAlmeida_Ficha06.py)

## Análise/comentário sobre a aula

> Os números aleatórios são fundamentais em diversas situações, entre elas a criptografia e a segurança informática, a simulação por computador ou os jogos.

Outras funções deste módulo: <https://docs.python.org/3/library/random.html>
