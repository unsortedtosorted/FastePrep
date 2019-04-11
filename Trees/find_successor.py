"""
Inorder Successor BST with Parent Pointers
The inorder successor of a node in a binary tree is the next node in an inorder traversal. 
Write a method to find an inorder successor of a given binary tree node in a 
binary search tree given parent pointers


Runtime : O(N)
Memo : O(H)
"""

def find_successor(root, d):

  stack = [root]
  lv = None
  
  while stack:
    
    if stack[-1]:
      stack.append(root.left)
      continue
    else:
      stack.pop()
      if stack:
        curr = stack.pop()
        if lv == d:
          return curr
        lv = curr.data
        stack.append(curr.right)
  
  return None
