"""
Ques: Given a singly linked list, return the nth from last node. Return null if 'n' is out-of-bounds.

1. Maintain 2 pointer, starting from head
2. move second pointer n-1 times
3. Move both pointers togerther now, untile second pointer has next
"""



def find_nth_from_last(head, n):
  #TODO: Write - Your - Code
  
  p1 = head
  p2 = head
  
  temp = n-1
  
  while temp>0:
    if not p2:
      return None
    p2 = p2.next
    temp-=1
  
  while p2 and p2.next:
    
    p1 = p1.next
    p2 = p2.next
    
    
  
  return p1
