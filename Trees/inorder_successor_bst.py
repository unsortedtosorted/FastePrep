"""
1. Do iterative inorder traversal of the tree
2. keep track of last value seen
3. if last value is equal to given value, then print it

"""


def inorder_successor_bst(root, d):
  
  stack = [root]
  
  lv = None
  
  while stack:
    
    if stack[-1]:
      
      stack.append(stack[-1].left)
      continue
    stack.pop()
    if stack:
      
      if lv == d:
        return stack[-1].data
      curr = stack.pop()
      lv = curr.data 
      stack.append(curr.right)
  
  return None
