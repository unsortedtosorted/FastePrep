"""
Given the head nodes of two linked lists that may or may not intersect, 
find out if they intersect and return the point of intersection. Return null otherwise.

1. start from head1 and head2
2. when curr1 reach end of list1 , make curr1 point to head2
3. when curr2 reach end of list2, make curr1 point to head1
4. if curr1 == curr2 , return curr1

"""


def intersect(head1, head2):
  
    
    p1 = head1
    p2 = head2
    
    once = False
    
    while p1 != p2:
      
      if p1:
        p1 = p1.next
      else:
        if not once:
          p1 = head2
        else:
          return None
      
      if p2:
        p2 = p2.next
      else:
        p2 = head1
    
    
    return p1
