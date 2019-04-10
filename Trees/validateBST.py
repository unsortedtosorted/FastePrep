"""

1. Do iterative inorder traversal 
2. check if curr value is greater than eqaul to last
value visited.

"""


def is_bst(root):
  #TODO: Write - Your - Code
  
  stack = [root]
  lv = -sys.maxsize-1
  
  while stack:
    
    curr = stack[-1]
    if curr:
      stack.append(curr.left)
      continue
    
    else:
      stack.pop()
      if stack:
        curr = stack.pop()
        if curr.data >= lv:
          lv = curr.data
          stack.append(curr.right)
        
        else:
          return False
      
  return True
