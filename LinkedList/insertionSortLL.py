"""

Given the head pointer of a linked list, sort it in ascending order using insertion sort.

1. create a new list, where we will inserted the node at correct position
2. insertion in new list can be 2 case:
    1. insert at head
    2. insert in middle
    
    Runtime : O(N^2)
    Space   : O(N)

"""



from LinkedList.linkedList import generateList
from LinkedList.linkedList import printll
from LinkedList.linkedList import Node


head = generateList([100,34,5,6,9,0,2,1])

sortedHead = Node()
sortedHead.val = head.val


prev = head
temp = head.next

while temp:



    #if less than sorted head

    if temp.val < sortedHead.val:

        toInsert = Node()
        toInsert.val = temp.val
        toInsert.next = sortedHead
        sortedHead = toInsert


    else:
        #if greater than head

        prev = sortedHead
        curr = sortedHead.next

        while curr and curr.val < temp.val:
            prev = curr
            curr = curr.next

        toInsert = Node()
        toInsert.val = temp.val
        prev.next = toInsert
        toInsert.next = curr

    temp = temp.next


print (printll(sortedHead))

