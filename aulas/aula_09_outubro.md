---
layout: default
---

# 9 de outubro de 2024

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
    - [Operadores de relação](#operadores-de-relação)
    - [Condições (if, else, elif)](#condições-if-else-elif)
    - [Operadores lógicos (and, or, not)](#operadores-lógicos-and-or-not)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise crítica à aula](#análise-crítica-à-aula)

---

## Conteúdos dados na aula

### Operadores de relação

- Igual: `a == b`
- Diferente: `a != b`
- Menor que: `a < b`
- Menor ou igual que: `a <= b`
- Maior que: `a > b`
- Maior ou igual que: `a >= b`

### Condições (if, else, elif)

#### If

> A instrução `if` aceita uma condição lógica que, caso seja verdadeira (True), executa um bloco de código. Caso a condição seja falsa (False), o bloco de código é ignorado. 

Exemplo:

```python
if 1 > 0:
    print("Verdadeiro")
```

Neste exemplo, como `1 > 0` é uma condição verdadeira, o bloco de código será executado, logo "Verdadeiro" será exibido no terminal.

#### Elif

> A instrução `elif` é utilizada para verificar várias condições sequencialmente. Se a condição de uma instrução anterior for falsa, a condição da próxima instrução `elif` será verificada. 

Exemplo:

```python
x = 3
if x == 1:
    print("x = 1")
elif x == 3:
    print("x = 3")
```

Neste exemplo, como `x == 1` é uma condição falsa, o bloco de código dentro da instrução `if` será ignorado e a condição `x == 3` será verificada. Como esta é verdadeira, "x = 3" será exibido no terminal.

#### Else

> A instrução `else` é utilizada para executar um bloco de código, caso a condição de uma instrução `if` seja falsa. 

Exemplo:

```python
if 1 > 2:
    print("Verdadeiro")
else:
    print("Falso")
```

Neste exemplo, como `1 > 2` é uma condição falsa, o bloco de código dentro da instrução `if` será ignorado e o bloco de código dentro da instrução `else` será executado. Deste modo, "Falso" será exibido no terminal.

### Operadores lógicos (and, or, not)

Os operadores lógicos `and`, `or` e `not` combinam condições lógicas e avaliam se uma dada expressão é verdadeira ou falsa.

#### And

> O operador lógico `and` avalia uma expressão como verdadeira caso ambas as condições que a compõemque a compõem sejam verdadeiras.

```python
if 1 > 0 and 2 > 3:
    print("Verdadeiro")
else:
    print("Falso")
```

Neste caso, como apenas a condição `1 > 0` é verdadeira, a expressão `1 > 0 and 2 > 3` é avaliada como falsa, logo "Falso" será exibido no terminal.

#### Or

> O operador lógico `or` avalia uma expressão como verdadeira caso pelo menos uma das condições que a compõem sejam verdadeiras.

```python
if 1 > 0 or 2 > 3:
    print("Verdadeiro")
else:
    print("Falso")
```

No exemplo acima, visto que a primeira condição, `1 > 0`, é verdadeira, a expressão `1 > 0 or 2 > 3` é avaliada como verdadeira. Assim, "Falso" será exibido no terminal.

#### Not

> O operador lógico `not` avalia uma expressão como verdadeira caso a condição que a compõe seja falsa.

```python
if not 2 > 3:
    print("Verdadeiro")
else:
    print("Falso")
```

Dado que a condição `2 > 3` é falsa, então a expressão `not 2 > 3` é avaliada como verdadeira, sendo exibido no terminal "Verdadeiro".

## Trabalho realizado na aula

Início da realização da [ficha 03](../trabalhos/D1_PedroAlmeida_Ficha03.py)

## Análise crítica à aula

---

<div style="max-width: fit-content; margin-left: auto; margin-right: auto; display: inline-block">
    <a href="https://1pedro.github.io/aplicacoesinf/aulas/aula_02_outubro.md"
        <button style="padding: 0;border: none; background: none"><img src="https://1pedroalmeida.github.io/aplicacoesinf/imgs/prev.png" width="50" height="50"/></button>
    </a>
    <a href="https://1pedro.github.io/aplicacoesinf/aulas/aula_11_outubro.md"
        <button style="padding: 0;border: none; background: none"><img src="https://1pedroalmeida.github.io/aplicacoesinf/imgs/next.png" width="50" height="50"/></button>
    </a>
</div>
