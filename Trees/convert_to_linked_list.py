"""
Given a binary tree, convert it to a doubly linked list so that the order of 
the doubly linked list is the same as an in-order traversal of the binary tree.

1. keep track of prev node
2. at curr node, make curr.left = prev and prev.right = curr

Runtime : O(N)
space : O(H)

"""


def convert_to_linked_list(root):
    
    head = None
    prev = None
    
    stack = [root]
    
    while stack:
      
      if stack[-1]:
        stack.append(stack[-1].left)
        continue
      stack.pop()
      if stack:
        curr = stack.pop()
        stack.append(curr.right)
        
        if not head:
          head = curr
        
        curr.left = prev
        if prev:
          prev.right = curr
        
        prev = curr
    
    prev.right = head
    
    return head
