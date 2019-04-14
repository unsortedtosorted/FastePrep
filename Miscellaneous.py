"""
Given a two-dimensional array, 
if any element within is zero, 
make its whole row and column zero.

"""

def make_zeroes(matrix):
  # TODO: Write - Your - Code
  
  visited = set()
  
  def change(i,j):
    #make all row element zero
    for r in range(0,len(matrix)):
      matrix[r][j] = 0
      visited.add((r,j))
    
    #make all col zero
    for col in range(0,len(matrix[i])):
      matrix[i][col] = 0
      visited.add((i,col))
                 
  
  
  
  for i,x in enumerate(matrix):
    
    for j,y in enumerate(x):
      
      if (i,j) not in visited and y == 0:
        change(i,j)
        visited.add((i,j))
  
  
  return matrix
