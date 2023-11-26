class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        newMatrix = []
        m = len(matrix)

        for j in range(m):
            aux = []
            for i in range(m):
                aux.append(matrix[i][j])
        aux.reverse()
        newMatrix.append(aux)
        matrix = newMatrix