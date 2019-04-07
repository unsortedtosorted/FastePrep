"""
Given the head pointers of two linked lists where each linked list represents 
an integer number (each node is a digit), add them and return the resulting linked list

At each step new node value = head1 + head2 + carry
"""



from LinkedList.linkedList import Node,generateList,printll

#head1 = generateList([1,3,4,5,9])
#head2 = generateList([0,0,3,1,9,9,9])

head1 = generateList([9,9,9,9,9,9,8])
head2 = generateList([1])

rHead = Node()
temp = rHead
carry = 0
sum = 0


while head1 or head2:

    if head1:
        sum += head1.val
        head1 = head1.next
    if head2:
        sum+= head2.val
        head2 = head2.next


    sum = sum+carry

    if sum > 9:
        carry = 1
        sum = sum-10
    else:
        carry = 0


    temp.val = sum
    sum = 0

    prev = temp
    temp.next = Node()
    temp = temp.next

if carry == 1:
    temp.val = 1

else:
    prev.next = None

print (printll(rHead))
