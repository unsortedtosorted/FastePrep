"""
Given a singly linked list, reverse the nodes at even indices.

Steps:

1. maintain 2 lists
2. remove even nodes and keep adding it to head of new list and delete from origin
3. Now mere two lists

RunTime : O(N)

"""



from LinkedList.linkedList import Node, generateList, printll


head1 = generateList([7,14,21,28,9])

def reverseEven(head):

    if not head or not head.next:
        return head


    prev = head
    curr = head.next
    temp = None
    n = 1

    print(printll(head))

    while curr:


        if n%2 == 1:
            #delete curr
            prev.next = curr.next

            #add to head of other list
            curr.next = temp
            temp = curr
            curr = prev.next

        else:
            prev = curr
            curr = curr.next

        n+=1

    #Megre two lists

    curr = head

    while temp:

        nex = temp.next

        temp.next = curr.next
        curr.next = temp

        temp = nex

        curr = curr.next.next

    return head
print (printll(reverseEven(head1)))
