#Dia 42 - Generate Parentheses
#Link para o Desafio: https://leetcode.com/problems/generate-parentheses/description/

#Enunciado:
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left: generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right: parens.append(p)
            return parens
        return generate('', n, n)