#Dia 16 - Criptografia RSA
#Sem link

#Dessa vez essa é uma atividade que eu mesmo estava fazendo, que se trata de utilizar o RSA para criar
#chave publica e descriptografar valores dos mesmos valores P e Q

#Gerar numeros aleatorios e primos
def rand():
  P = Q = 10
  while True:
    P = random.randint(11, 200)
    Q = random.randint(13, 200)

    if primo(P) and primo(Q) and P != Q:
      break
  return P, Q


#Verificar se numero é primo
def primo(numero):
  if numero < 2:
    return False
  for num in range(2,int(numero ** 0.5) + 1):
    if numero % num == 0:
      return False
  return True


#Encontrar Minimo divisor Comum entre dois numeros
def mdc(a, b):
    while b:
      a, b = b, a % b
    return a


#Calcular valores de N, Z, D, E
def calcula(P, Q):
  #Achando N
  N = P * Q

  #Achando Z
  Z = (P - 1) * (Q - 1)

  D = random.randint(3, 100)
  E = 2

  #Achando D -
  contador = 1

 # Encontrar um número D que seja relativamente primo a Z
  while mdc(D, Z) != 1:
    D += 1

  #Achando E
  while (E * D) % Z != 1:
      E += 1

  return N, Z, E, D


#Função para descriptografar
def descriptografar(criptografado, D, N):
  descriptografado = ''
  for carac in criptografado:
    preparo = pow(ord(carac), D, N)
    descriptografado += chr(preparo)
  return descriptografado

import random
from time import sleep
from IPython.display import clear_output

def anima(frase):
    carregamento = ''
    for tempo in range(3):
      carregamento += '.'
      print(carregamento)
      sleep(0.5)
      clear_output()
    print("{}".format(frase))
    sleep(1)
    clear_output()

def entrarPQ(PQ):
  while True:
    try:
      PQ = int(input(""))
      if primo(PQ):
        print("Aceito!")
        sleep(1)
        clear_output()
        return PQ
      else:
        print("Valor não primo!")
    except ValueError:
      print("Entrada inválida. Você deve digitar um número inteiro.")


def menu():
  P = Q = Z = N = E = D = 0
  while True:
    print("==============================================================")
    print("--------------------------------------------------------------")
    print("|P = ",P)
    print("|Q = ",Q)
    print("|E = ",E)
    print("|D = ",D)
    print("|Chave publica (E,N): ({},{})".format(E, N))
    print("==============================================================")
    print("--------------------------------------------------------------")
    print("|[1] - Gerar chave automaticamente")
    print("|[2] - Selecionar valores da chave")
    print("|[3] - Descriptografar")
    print("|[4] - Ver chave privada")
    print("|[0] - Encerrar")
    print("--------------------------------------------------------------")
    print("==============================================================")

    try:
      entrada = 0
      entrada = int(input("Entrada: "))
    except ValueError:
      clear_output()
      print("Entrada inválida. Você deve digitar um número inteiro.")
      sleep(1)
      continue

    #Encerrar
    if entrada == 0:
      clear_output()
      break

    # Gerar chave
    if entrada == 1:
      P, Q = rand()
      N, Z, E, D = calcula(P,Q)
      clear_output()
      anima("Calculado!")

    # Selecionar chave
    elif entrada == 2:
      P = Q = Z = N = E = D = 0
      clear_output()
      print("==============================================================")
      print("|P: ")
      P = entrarPQ(P)
      print("|Q: ")
      Q = entrarPQ(Q)
      N, Z, E, D = calcula(P,Q)
      clear_output()
      anima("Calculado!")

    #Descriptografar
    elif entrada == 3:
      if D == 0:
        clear_output()
        print("Crie uma chave primeiramente!")
        sleep(1)
        clear_output()
      else:
        conjunto = str(input("Digite a string criptografada: "))
        descriptografado = descriptografar(conjunto, D, N)
        clear_output()
        anima("Descriptografado!")

        saida = 1
        while True:
          print("==============================================================")
          print("--------------------------------------------------------------")
          print("|Versão Criptografada:    <{}>".format(conjunto))
          print("|Versão Descriptografada: <{}>".format(descriptografado))
          print("--------------------------------------------------------------")
          print("==============================================================")
          saida = ''
          saida = str(input("Digite 0 para sair: "))
          if saida == '0':
            clear_output()
            break
          clear_output()

        else:
          print('Entrada inválida!')

    #Mostrar Chave
    elif entrada == 4:
      clear_output()
      while True:
        print("==============================================================")
        print("--------------------------------------------------------------")
        print("|Chave privada (D,N): ({},{})".format(D, N))
        print("--------------------------------------------------------------")
        print("==============================================================")
        saida = ''
        saida = str(input("Digite 0 para sair: "))
        if saida == '0':
          clear_output()
          break
        else:
          print('Entrada inválida!')

    #Entrada inválida
    else:
      print('Entrada Inválida!')
      clear_output()

menu()