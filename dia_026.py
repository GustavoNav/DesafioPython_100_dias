#Dia 26 - Longest Common Prefix
#Link para o Desafio: https://leetcode.com/problems/longest-common-prefix/description/

#Enunciado:
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            prefix = strs[0]
            for string in strs:
                while string[:len(prefix)] != prefix and prefix:
                    prefix = prefix[:-1]
                    if not prefix:
                        return ""
            
            return prefix