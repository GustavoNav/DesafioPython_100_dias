#Dia 4 - Soma de Fatoriais
#Link do Desafio: https://www.beecrowd.com.br/judge/pt/problems/view/1161

#Enunciado
'''
Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.

Entrada
O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 ≤ M ≤ 20) e N (0 ≤ N ≤ 20). O fim da entrada é determinado por eof.

Saída
Para cada caso de teste de entrada, seu programa deve imprimir uma única linha, contendo um número que é a soma de ambos os fatoriais (de M e N).
'''


while True:
    try:
        fa1, fa2 = map(int, input().split())

        fa1 = 1 if fa1 == 0 else fa1
        fa2 = 1 if fa1 == 0 else fa2

        fa1Tot = 1
        fa2Tot = 1
        for num in range(fa1, 0, -1):
            fa1Tot *= num

        for num in range(fa2, 0, -1):
            fa2Tot *= num

        print(fa1Tot + fa2Tot)
    except EOFError:
        break