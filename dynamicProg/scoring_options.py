"""

ways to reach n = ways to reach(n-1) + ways to reach(n-2) + ways to reach(n-4)  

"""


#Scoring options are 1, 2, 4
def scoring_options(n):
  #TODO: Write - Your - Code
  
  memo = {}
  def dp(remain):
    
    if remain in memo:
      return memo[remain]
    
    if remain < 0:
      return 0
    if remain == 0:
      memo[remain] = 1
      return 1
    else:
      x = dp(remain-1)
      y = dp(remain-2)
      z = dp(remain-4)
      memo[remain] = x+y+z
      return memo[remain]
      
  return dp(n)
  
