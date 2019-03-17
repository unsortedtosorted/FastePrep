"""
Given the head of a singly linked list and 'N', 
swap the head with the Nth node. Return the head of the new linked list.

Algo:
  
  1. Do next curr = curr.next n-1 times
  2. swap value of head with curr
  3. return head


"""


def swap_nth_node(head, n):
  
  curr = head
  while n>1:
    
    if curr:
      curr = curr.next
      n-=1
    else:
      return None
  
  temp = head.data
  
  head.data = curr.data
  curr.data = temp
    
  return head
