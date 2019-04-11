"""
Delete Zero Sum Sub-Trees
Given the root of a binary tree, delete any subtrees whose nodes sum up to zero.

1. delete_zero_sum_subtree left sub tree
2. delete_zero_sum_subtree right sub tree
3. return root.val + left subtree sum +right subtree sum

Runtime : O(N)
Memory :  O(h) 

Recursive solution has O(h) memory complexity as it will consume memory 
on the stack up to height of binary tree h. 
It will be O(logn) for balanced tree and in the worst case can be O(n).


"""


def delete_zero_sum_subtree(root):
  def delesumsub(root):
    
    
    if root:
      
      if root.left or root.right:
        
        lsum = delesumsub(root.left)
        rsum = delesumsub(root.right)
        
        if lsum == 0:
          root.left = None
        if rsum == 0:
          root.right = None
          
        return root.data+lsum+rsum
          
      
      else:
        return root.data

      

  delesumsub(root)
  return root
