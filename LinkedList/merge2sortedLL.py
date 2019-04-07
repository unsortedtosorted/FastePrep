"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

Runtime : O(M+N)

"""


from LinkedList.linkedList import generateList
from LinkedList.linkedList import printll
from LinkedList.linkedList import Node


head1 = generateList([2,13,25,67,89,100])
head2 = generateList([13,99,123,345,456,790])


newHead = Node()
temp = newHead

while head1 or head2:

    if head1 and head2:

        temp.next = Node()
        if head1.val <= head2.val:
            temp.val = head1.val
            head1 = head1.next
        else:
            temp.val = head2.val
            head2 = head2.next
        prev = temp
        temp = temp.next


    else:
        break



if head1 and not head2:
    prev.next = head1
if head2 and not head1:
    prev.next = head2


print (printll(newHead))

