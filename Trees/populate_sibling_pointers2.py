"""
Given the root to a binary tree where each node has an additional pointer called a sibling (or next), 
connect the sibling pointer to the next node in the same level. 
The last node in each level should point to the first node of the next level in the tree


1.Do level order traversal
2.keep track of prev node
3.make prev.next = currNode

"""

from collections import deque

def populate_sibling_pointers(root):
  
  q = deque()
  q.append(root)
  prev = None
  
  while q:
    
    curr = q.pop()
    
    if curr.left:
      q.appendleft(curr.left)
    if curr.right:
      q.appendleft(curr.right)
    
    if prev:
      prev.next = curr
    
    prev = curr
    
  return root
