#Dia 34 - Majority Element
#Link para o Desafio: https://leetcode.com/problems/majority-element/description/

#Enunciado:
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        v = {}
        for num in nums:
            if num not in v:
                v[num] = 1
            else:
                v[num] += 1

        return max(v, key=v.get)
