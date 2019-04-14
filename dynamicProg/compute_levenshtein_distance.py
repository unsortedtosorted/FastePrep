"""
Compute the Levenshtein distance between two strings.

try all 3 option :
  insert
  delte
  replace
  
  replace the min 

"""


def compute_levenshtein_distance(str1, str2):
  
   
  def dp(i,j):
    
    if i >= len(str1):
      if j < len(str2):
        return len(str2)-j
      else:
        return 0
    if j >= len(str2):
      if i < len(str1):
        return len(str1)-i
      else:
        return 0
    
    if str1[i] == str2[j]:
      return dp(i+1,j+1)
    else:
      
      #insert
      x1 = 1+dp(i+1,j)
      #delete
      x2 = 1+dp(i,j+1)
      #replace
      x3 = 1+dp(i+1,j+1)
      
      return min(x1,x2,x3)
      

  return dp(0,0)
