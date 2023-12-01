#Dia 25 - Swap Nodes in Pairs
#Link para o Desafio: https://leetcode.com/problems/swap-nodes-in-pairs/description/

#Enunciado:
'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem 
without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Iniciando a inversão dos pares
        prev = None
        current = head

        while current and current.next:
            # Salvando os nós que serão invertidos
            first = current
            second = current.next

            # Invertendo os pares
            first.next = second.next
            second.next = first

            # Conectando o par invertido com o resto da lista
            if prev:
                prev.next = second
            else:
                head = second

            # Atualizando os ponteiros para o próximo par
            prev = first
            current = first.next
            
        return head