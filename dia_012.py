#Dia 12 - Add Two Numbers
#link para o Desafio: https://leetcode.com/problems/add-two-numbers/description/

#Enunciado
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = []
        num2 = []
        
        #Armazenar valores de l1 em uma lista
        current_node = l1
        while current_node is not None:
            num1.append(current_node.val)
            current_node = current_node.next

        #Armazenar valores de l2 em uma lista
        current_node = l2
        while current_node is not None:
            num2.append(current_node.val)
            current_node = current_node.next

        #Inverter as listas
        num1 = num1[::-1]
        num2 = num2[::-1]

        n1 = ''
        n2 = ''

        #Transformar o valor de n1 e n2 em um inteiro
        for i in num1:
            n1 += str(i)
        for i in num2:
            n2 += str(i)

        n1 = int(n1)
        n2 = int(n2)
        
        #Somar valores e então converter para uma string
        n3 =  n1 + n2
        n3 = str(n3)

        result = []

        #Criar uma lista com os valores
        for i in n3:
            result.append(int(i))

        #Inverter a lista
        result = result[::-1]
        
        #Criar head e tail para armazenar os valores na estrutura
        head = ListNode(result[0])
        tail = head
        
        #Deifinir 1 para percorrer a estrutura
        i = 1
        #Enquanto não percorer toda a distancia da lista
        while i < len(result):
            #Proximo valor de tail recebe o indice i da lista
            tail.next = ListNode(result[i])
            #tail recebe seu o tail.next
            tail = tail.next
            #incrementar o indice
            i += 1
        
        #retornar a estrutura
        return head