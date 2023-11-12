#Dia 6 - Reverse Integer
#Link do Desafio: https://leetcode.com/problems/reverse-integer/

#Enunciado

'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution(object):
    def reverse(self, x):
        aux = ''
        auxT = str(x)
        if auxT[0] == '-':
            auxT = auxT[::-1]
            auxT = '-' + auxT[:len(auxT) - 1]
        else:
            auxT = auxT[:: -1]
        if int(auxT) > 2**31 or int(auxT) < -2**31:
            return 0
        else:
            return int(auxT)