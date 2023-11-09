# -*- coding: utf-8 -*-
"""dia_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KxRESG2sVYMCKlj9FWyeBNpXL4-xbFya
"""

#Dia 3 - Balanço de Parênteses I
#Link para desafio: https://www.beecrowd.com.br/judge/pt/problems/view/1068

#Enunciado
'''
Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em conta o restante da expressão. Por exemplo:

a+(b*c)-2-a        está correto
(a+b*(2-c)-2+a)*2  está correto

enquanto

(a*b-(2+c)         está incorreto
2*(3-a))           está incorreto
)3+b*(2-c)(        está incorreto

Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parênteses que fecha sem um previo parenteses que abre e a
quantidade total de parenteses que abre e fecha deve ser igual.

Entrada
Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as palavras correct ou incorrect de acordo com as regras acima fornecidas.
'''

#Lista de linhas
linhas = []

#Entradas de linhas enquanto ouver linhas
while True:
  try:
    line = input()
    if not line:
      break
    linhas.append(line)
  except EOFError:
    break

#numero de parenteses aberto
aberto = 0
#numero de parenteses fechados
fechado = 0
for linha in linhas:
  for carac in linha:
    if carac == ')':
      fechado += 1
    if fechado > aberto:
      fechado += 1
      
    if carac == '(':
      aberto += 1
  if aberto == fechado:
    print("correct")
  else:
    print("incorrect")
  aberto = 0
  fechado = 0