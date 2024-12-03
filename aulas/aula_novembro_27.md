---
layout: default
---

# 27 de novembro de 2024

<h3><b>Índice</b></h3>

1. [Conteúdos dados na aula](#conteúdos-dados-na-aula)
2. [Trabalho realizado na aula](#trabalho-realizado-na-aula)
3. [Análise/comentário sobre a aula](#análisecomentário-sobre-a-aula)

---

## Conteúdos dados na aula

### Strings

As variáveis do tipo `string` (cadeias de caracteres) permitem armazenar, em memória, palavras, frases ou outras combinações de caracteres.

Em python, uma `string` é delimitada por aspas (" ") ou por plicas (' '), símbolos que marcam o início e fim de uma `string`.

##### Exemplos:

```python
nome = "Pedro"
frase = "Isto é uma frase."
letras = "abcdefABCDEF"
numeros = "1234567890"
```

### Caracteres

Para armazenar em memória um único carácter, em python, recorremos a variáveis do tipo `string`. Existe também a noção de `string` vazia.

```python
str_letra = "A"
str_vazia = ""
```

Podemos também aceder aos caracteres individuais de uma `string` referenciando a sua posição, entre parêntesis retos [].

O primeiro carácter encontra-se na posição 0, o segundo na posição 1, o terceiro na posição 2 e assim sucessivamente, conforme o número de caracteres da `string`.

```python
str = "ABC"

print(str[0]) # A

c = string[2]
print(c) # C

print(string[1]) # B
```

### Tamanho de uma string

O tamanho de uma `string`, isto é o número de caracteres que ela contém, pode ser obtido através da instrução `len`.

```python
str = "ABC"
n = len(str)

print(n) # 3
```

### Identificação de caracteres

Adicionalmente, cada carácter individual tem uma representação númerica. Existem várias formas de codificação de caracteres, sendo a ASCII e a UNICODE as mais comuns.

Em python, podemos trabalhar com esta tal representação numérica através das instruções `chr` e `ord`.

```python
print(chr(65)) # A
print(ord("A")) # 65
```

#### Tabela ASCII

<img src="https://1pedroalmeida.github.io/aplicacoesinf/imgs/ascii_table.jpg" height="600"/>

## Trabalho realizado na aula

Início da realização da [ficha 7](../trabalhos/D1_PedroAlmeida_Ficha07.py)

## Análise/comentário sobre a aula

#### Links relevantes:

- Documentação adicional relativa às strings em python: <https://docs.python.org/3/library/stdtypes.html#string-methods>
- Strings num contexto geral da programação: <https://pt.wikipedia.org/wiki/Cadeia_de_caracteres>
- Sistemas de representação de texto:
    - ASCII: <https://pt.wikipedia.org/wiki/ASCII>
    - UNICODE: <https://pt.wikipedia.org/wiki/Unicode>
