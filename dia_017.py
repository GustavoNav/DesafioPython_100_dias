#Dia 16 - Criptografia RSA - PARTE 2
#Sem link

#Essa é a continuação do meu código de criptografia, dessa vez uma parte focada no recebimento de uma 
#string e da chave publica para realizar a criptografia 

#Função para criptografar
def criptografar(palavra, E, N):
  criptografado = ""
  for carcter in palavra:
    preparo = pow(ord(carcter), E, N)
    criptografado += chr(preparo)
  return criptografado

  # Criptografar

conjunto = str(input("Digite uma String: "))
chave = str(input("Digite a chave pública (E, N): \t"))