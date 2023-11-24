#Dia 19 - Valid Sudoku
#Link para o desafio: https://leetcode.com/problems/valid-sudoku/

#Enunciado
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the 
following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            valuesR = []
            for col in row:
                if col not in valuesR and col != '.':
                    valuesR.append(col)
                elif col in valuesR and col != '.':
                    return False

        for c in range(0 , 9):
            valuesC = []
            for r in range(0 , 9):
                if board[r][c] not in valuesC and board[r][c] != '.':
                    valuesC.append(board[r][c])
                elif board[r][c] in valuesC and board[r][c] != '.':
                    return False
        
        # Lista para armazenar os conjuntos 3x3
        conjuntos = []

        # Iterar sobre a matriz em etapas de 3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Coletar o conjunto 3x3
                conjunto = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                # Adicionar o conjunto à lista de conjuntos
                conjuntos.append(conjunto)


        for r in conjuntos:
            values3x3 = []
        for c in r:
            if c not in values3x3 and c != '.':
                values3x3.append(c)
            elif c in values3x3 and c != '.':
                return False
         
        return True