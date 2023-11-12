#Dia 8 - Median of Two Sorted Arrays
#link para o desafio: https://leetcode.com/problems/median-of-two-sorted-arrays/

#Enunciado:
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Unir as duas listas.
        merged = nums1 + nums2
        #Ordenar a lista.
        merged.sort()
        
        #Encontrar o indice da lista.
        n = len(merged)
        #Encontrar a metade da lista, é necessário subtrair 1 pois a contagem de listas começa no indice 0.
        m = len(merged) // 2 - 1
        result = 0

        
        if n % 2 != 0:
            #Se a lista ser impar, a media é simplismente a metade do indice + 1, o seu meio.
            result = merged[m + 1]
        else:
            #Caso a lista seja par, precisamos somar os 2 numeros no meio e dividir por 2.
            result = (merged[m] + merged[m + 1]) / 2
        
        #Retornar a Mediana
        return result