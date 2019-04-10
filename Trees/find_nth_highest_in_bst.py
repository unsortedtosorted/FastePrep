"""
Do iterative reverse inorder traversal of bst

"""


def find_nth_highest_in_bst(node, n ):
  
  stack = [node]
  x = 0
  while stack:
    
    curr = stack[-1]
    
    if curr:
      stack.append(curr.right)
      continue
    
    stack.pop()
    if stack:

      curr = stack.pop()
      x+=1
      if x == n:
        return curr
      stack.append(curr.left)
      
  return None
