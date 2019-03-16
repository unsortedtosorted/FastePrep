"""

Delete a given node from the linkedList:

If given key is the head node --> return head.next

else:
     for curr node if there is next node 
     and next node is equal to key
     delete next node.


"""


def delete_node(head, key):
  
  
  if head and head.data == key:
    return head.next
  
  curr = head
  
  while curr:
    
   
    temp = curr.next
    
    if temp and temp.data == key:
      curr.next = temp.next
      break
    
    curr = curr.next
  
  
  return head
