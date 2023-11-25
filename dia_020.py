#Dia 20 - Numeros Felizes
#Não possui link

#Enunciado
'''
Hoje eu vi um video que falava so numeros felizes:
Se tratam de numeros que quando pegamos seus valores, elevamos ao quadrado e então
somamos, ao repetir o processo por n vezes, o resultado sempre dará o numero 1.
Por exemplo:
19
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Logo, o numero 19 é feliz.
Vou escrever um programa para ver todos os numeros felizes dentro de um range
'''

def feliz(lista):
  resultado = 0
  for v in lista:
    resultado += int(v) ** 2
  return resultado

final = []
for num in range(0, 100):
  resultado = 0
  contador = 0
  aux = num
  while resultado != 1:
    valores = list(str(aux))
    resultado = feliz(valores)
    aux = resultado
    contador += 1
    if contador == 10:
      break
  if resultado == 1:
    final.append(num)


print(final)