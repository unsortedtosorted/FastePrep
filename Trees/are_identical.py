"""

Given the roots of two binary trees, determine if these trees are identical or not.

Algo:
  1. Do inorder traversal together
  2. if root1.val == root2.val
    - inorder(root1.left,root2.left)
    - inorder(root2.right,root2.right)
  3. else:
      return False
      
    

"""

def are_identical(root1, root2):
 
  arr = [True]

  def inorder(root1,root2):
    
    if root1 and root2:
      if root1.data == root2.data:
        inorder(root1.left,root2.left)
        inorder(root1.right,root2.right)
      else:
        arr[0] = arr[0] & False
    elif root1 and not root2:
      arr[0] = arr[0] & False
    elif not root1 and root2:
      arr[0] = arr[0] & False
      
  inorder(root1,root2)    
  return arr[0] 
