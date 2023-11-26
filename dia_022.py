#Dia 22 - Number of Islands
#Link para o Desafio: https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

#Enunciado
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
n = len(grid)
m = len(grid[0])

tot = 1

for i in range(1, n-1):
  for j in range(m - 1):
      #print(grid[i-1][j], " ",grid[i][j], " ",grid[i+1][j])
      #print(grid[i][j-1], " ",grid[i][j], " " , grid[i][j+1])
      #print(grid[i][j-1], grid[i][j], grid[i][j+1])
      #print(grid[i+1][j])
      if grid[i-1][j] == '0' and grid[i][j-1] == '0' and  grid[i][j] == '1' and grid[i][j+1] == '0' and grid[i+1][j] == '0':
        tot+=1


for j in range(m):
  if j == 0:
    if grid[0][j] == '1' and grid[0][j+1] == '0' and grid[1][j] == '0':
      tot+=1
  elif j == m-1:
    if grid[0][j-1] == '0' and grid[0][j] == '1' and grid[1][j] == '0':
      tot+=1
  else:
    if grid[0][j-1] == '0' and grid[0][j] == '1' and grid[0][j+1] == '0' and grid[1][j] == '0':
      tot+=1

for j in range(m):
  if j == 0:
    if grid[n-1][j] == '1' and grid[n-1][j+1] == '0' and grid[n-2][j] == '0':
      tot+=1
  elif j == m-1:
    if grid[n-1][j-1] == '0' and grid[n-1][j] == '1' and grid[n-2][j] == '0':
      tot+=1
  else:
    if grid[n-1][j-1] == '0' and grid[n-1][j] == '1' and grid[n-1][j+1] == '0' and grid[n-2][j] == '0':
      tot+=1

return tot