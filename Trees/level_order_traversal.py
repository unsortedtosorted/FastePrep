from collections import deque

def level_order_traversal(root):
  result = ""
  #TODO: Write - Your - Code
  q = deque()
  q.append(root)
  
  while q:
    
    curr = q.pop()
    if curr:
      result = result + str(curr.data)+" "
      q.appendleft(curr.left)
      q.appendleft(curr.right)
    
 

  return result
