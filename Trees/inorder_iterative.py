"""
Write an inorder traversal of a binary tree iteratively.

1. check top of stack, if not none
2. keep adding left of curr to stack
3. if none:
    -- pop top (remove none)
    -- curr = pop  (to print value)
    -- add curr.left tp stack
    
    
Runtime : O(N)


"""



def inorder_iterative(root):
  result = ""
  
  
  stack  = [root]
  
  
  while len(stack) > 0:
    
    curr = stack[-1]
    
    if curr:
      stack.append(curr.left)
      continue
    
    stack.pop()
    if stack:
      curr = stack.pop()
      result = result + str(curr.data)+ " " 
      stack.append(curr.right)
  return result
