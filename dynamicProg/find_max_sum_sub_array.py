"""
Largest Sum Subarray
Given an array, find the contiguous subarray with the largest sum.

1. a new array can start at every index
2. decision to start a new array should be made at index i if prev sum is less than zero

dp equation : 
    dp(i) = max(dp(i-1),0) + A[i]
    

Runtime : O(N)

"""

import sys
def find_max_sum_sub_array(A):
  #TODO: Write - Your - Code

  m = [-sys.maxsize-1]
  def dp(i):

    if i == 0:
      return A[i]
    else:

      s = max(dp(i-1),0)+A[i]
      m[0] = max(s,m[0])
      print (s)
      return s


  dp(len(A)-1)  
  return m[0]
