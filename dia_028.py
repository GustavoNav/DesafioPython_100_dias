#Dia 28 - Merge Two Sorted Lists
#Link para o Desafio: https://leetcode.com/problems/merge-two-sorted-lists/description/

#Enunciado:
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        tail1 = list1
        tail2 = list2
        while tail1 != None:
            values.append(tail1.val)
            tail1 = tail1.next

        while tail2 != None:
            values.append(tail2.val)
            tail2 = tail2.next
  
        dummy = ListNode()
        current = dummy
        for val in sorted(values):
            current.next = ListNode(val)
            current = current.next

        return dummy.next