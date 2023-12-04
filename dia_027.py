#Dia 27 - Group Anagrams
#Link para o Desafio: https://leetcode.com/problems/group-anagrams/description/


#Enunciado:
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in seen:
                seen[sorted_word] = [word]
            else:
                seen[sorted_word].append(word)


        result = list(seen.values())

        return result