"""
Given the pointer/reference to the head of a singly linked list, 
reverse it and return the pointer/reference to the head of reversed linked list


Maintain 3 pointer :
  prev
  curr
  next
  
  keep doind until next is there:
    
    nex = curr.next
    curr.next = prev
    prev = curr
    curr = nex
    
    
    Runtime : O(N)
    Memory : O(1)

"""




def reverse_iterative(head):
  reversed_list = head
  #TODO: Write - Your - Code
  
  if not head:
    return head
  
  prev = None
  curr = head
  
  while curr:
    
    nex = curr.next
    curr.next = prev
    prev = curr
    curr = nex
    
  return prev
