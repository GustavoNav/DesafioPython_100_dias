#Dia 7 - Caracteres faltando

#Link: Essa atividade não possui  um link, pois foi feita durante uma questão de um teste de python que eu fiz na HackerRank (passei nele).

#Enunciado descrito por mim
'''
Praticamente preciso receber uma string, e então dizer todos as letras do alfabeto 
estão faltando nela na ordem, além disso, o mesmo vale para numeros.
'''
def missingCharacters(s):
  #Variavel para armazenar saida
  result = ''
  #Lista onde armazeno todos os caracteres na string
  listA = []

  for charc in s:
      listA.append(charc)
 
  #Buscar valores numericos nao presentes e adicionar ao resultado
  for num in range(0,10):
      if str(num) not in listA:
          result += str(num)
  #Buscar as letras nao presentes e adicionar ao resultado
  for letter in range(97, 123):
      if chr(letter) not in listA:
          result += chr(letter)