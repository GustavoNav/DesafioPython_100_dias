#Dia 9 - Pow(x,n)
#link para enunciado: https://leetcode.com/problems/powx-n/
#Fonte de Binary Exponentiation: https://www.geeksforgeeks.org/binary-exponentiation-for-competitive-programming/

'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Resolução com exponencialização binária

        #Variável auxiliar
        v = n

        resultado = 1
        #Transformar valor negativo em positivo
        if v < 0:
            v *= -1
        
        #Aplicação da exponencialização binária
        while v > 0:
            if v % 2 == 1:
                resultado *= x
            x *= x
            v //= 2
        #Caso valor negativo, aplicar propriedade do expoente negativo: dividir 1.
        if n < 0:
            resultado = 1 / resultado

        return resultado