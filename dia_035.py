#Dia 35 - Reverse Nodes in k-Group
#Link para o Desafio: https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/

#Enunciado:
'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]


Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
'''

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        result = head
        count = 0
        values = []

        while current != None:
            values.append(current.val)
            count += 1
            current = current.next
            if count == k:
                count = 0
                values.reverse()
                while result != None:
                    if count == k:
                        count = 0
                        break
                    result.val = values[count]
                    result = result.next
                    count += 1
                values = []
        return head