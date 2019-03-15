"""
Given three integer arrays sorted in ascending order, 
have to find the smallest number that is common in all three arrays.


Algo:

  1. Maintain 3 pointer pointing to 0 index of all arrays
  2. Find max of all the 3 i.e a[0], b[0] and c[0]
  3. if a,b,c[curr]< max increment curr
  4. if a[curr1] = b[curr2] = c[curr3] --> return a[curr1]
  5. if curr1>=len(a) or curr2 >= len(b) or curr3 >= len(c) return -1
  
"""

def find_least_common_number(a,b,c):
   
    curr1 = 0
    curr2 = 0
    curr3 = 0
    while (True):
      
      if curr1 >= len(a):
        return -1
      
      if curr2 >= len(b):
        return -1
      
      if curr3 >= len(c):
        return -1
       
      A = a[curr1]
      B = b[curr2]
      C = c[curr3]
      
      M = max(A,B,C)
      if A == B and A == C:
        return A
      
      if A<M:
        curr1+=1
      if B<M:
        curr2+=1
        
      if C<M:
        curr3+=1
