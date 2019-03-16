"""

Given a LinkedList remove duplicate nodes:

Algorithm:
  1. curr = head node
  2. add curr.data to set
  3. temp = curr.next
  4. while temp.data is in set:
      temp = temp.next
  5. curr.next = temp
  6. curr = temp
  7. if curr is None --> break
  8. return Head
  
  
  Runt time : O(N)
  


"""




def remove_duplicates(head):
  #TODO: Write - Your - Code
  
  s = set()
  
  curr = head
  while curr:
    
    s.add(curr.data)
    nex = curr.next
    
    while nex and nex.data in s:
      nex = nex.next
    
    
    curr.next = nex
    curr = nex
  
  return head
