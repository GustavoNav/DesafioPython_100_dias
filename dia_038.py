#Dia 38 - Longest Palindromic Substring
#Link para o Desafio: https://leetcode.com/problems/longest-palindromic-substring/description/

#Enunciado:
'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''


#Versão 1 - (Lento)
class Solution:
    def longestPalindrome(self, s: str) -> str:
            n = len(s)
            longest = s[0]
            for c in range(n):
                sub = s[c:]
                for j in range(n):
                    sub = sub[:n-j]
                    if sub == sub[::-1]:
                        if len(sub) > len(longest):
                            longest = sub

#Versão 2 - (Dinâmico)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans