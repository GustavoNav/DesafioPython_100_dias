#Dia 39 - Binary Tree Postorder Traversal
#Link para o Desafio: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

#Enunciado:
'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)
                return result
        return traverse(root)