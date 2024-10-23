---
layout: default
---

# 23 de outubro de 2024

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise crítica à aula](#análise-crítica-à-aula)

---

## Conteúdos dados na aula

### Turtle

#### Exploração de outras funções da biblioteca para além das mencionadas na [aula anterior](aula_18_outubro.md).

| Instrução | Descrição |
| --- | --- |
| fillcolor() | Definir a cor de preenchimento |
| begin_fill() | Definir o início do preenchimento de uma forma a ser desenhada |
| end_fill() | Preencher a forma desenhada |

#### Exemplo

##### Desenhar quatro círculos de cores diferentes como apresentado na figura

<img src="https://1pedroalmeida.github.io/aplicacoesinf/imgs/aula_23_outubro_circulos.png" height="64"/>

```python
import turtle

for i in range(4):
    if i == 0:
        turtle.fillcolor("blue")
    elif i == 1:
        turtle.fillcolor("yellow")
    elif i == 2:
        turtle.fillcolor("pink")
    else:
        turtle.fillcolor("red")

    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
```

## Trabalho realizado na aula

Continuação da realização da [ficha 4](../trabalhos/D1_PedroAlmeida_Ficha04.py)

## Análise crítica à aula

