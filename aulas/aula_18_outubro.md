---
layout: default
---

# 18 de outubro de 2024

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise crítica à aula](#análise-crítica-à-aula)

---

## Conteúdos dados na aula

### Turtle

> A biblioteca turtle é uma implementação das ferramentas introduzidas pela linguagem de programação [LOGO](https://pt.wikipedia.org/wiki/Logo) em Python que oferece funcionalidades gráficas simples de usar.
> 
> O conceito da biblioteca envolve uma tartaruga que, à medida que se movimenta, consegue desenhar e pintar por onde passa.

#### Importar a biblioteca Turtle

```python
import turtle
```

#### Funções básicas

| Instrução | Versão curta | Descrição |
| --- | --- | --- |
| forward() | fd() | Mover para a frente o número de passos indicado |
| backward() | bk() ou back() | Mover para trás o número de passos indicado |
| right() | rt() | Rodar no sentido horário o ângulo indicado |
| left() | lt() | Rodar no sentido anti-horário o ângulo indicado |
| pendown() | pd() ou down() | Baixar a caneta (permite desenhar) |
| penup() | pu() ou up() | Levantar a caneta (deixa de desenhar) |
| hideturtle() | ht() | Ocultar a figura da ‘tartaruga’ |
| showturtle() | st() | Mostrar a figura da ‘tartaruga’ |
| setposition() | setpos() ou goto() | Posicionar nas coordenadas indicadas |
| dot() | n/a | Marcar um ponto na localização corrente |
| circle() | n/a | Desenhar um círculo |
| clear() | n/a | Apagar todos os desenhos no ecrã |

#### Exemplos

1. Desenhar um triângulo

```python
import turtle

turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
```

2. Desenhar um círculo de raio 60

```python
import turtle

turtle.circle(60)
```

3. Desenhar um quadrado e depois apagá-lo

```python
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.clear()
```

## Trabalho realizado na aula

- Conclusão da realização da [ficha 3](../trabalhos/D1_PedroAlmeida_Ficha03.py)
- Início da realização da [ficha 4](../trabalhos/D1_PedroAlmeida_Ficha04.py)

## Análise crítica à aula

