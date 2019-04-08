"""
Copy Linked List with Arbitrary Pointer

1. First copy each node normally
2. store each node based on value in hasmap
3. again copy node, this time with arbitrary pointers

Runtime : O(N)
space : O(N)
"""

def deep_copy_arbitrary_pointer(head):
   #TODO: Write - Your - Code
    
    temp = head
    new_head = LinkedListNode(head.data)
    temp2 = new_head 
    temp = temp.next
    ab = {}
    ab[head.data] = new_head
    
    while temp:
      
      temp2.next = LinkedListNode(temp.data)
      temp = temp.next
      temp2 = temp2.next
      ab[temp2.data] = temp2
      
      
    temp2 =  new_head
    temp = head
    
    while temp:
      if temp.arbitrary:
        temp2.arbitrary = ab[temp.arbitrary.data]
      temp2 = temp2.next
      temp = temp.next

    return new_head
