"""

Given the head node of a singly linked list and an integer 'n', rotate the linked list by 'n'.

1. adjust value of n
2. find lenght of list
3. go to N-nth Node
4. make N-nth node newhead that will be returned
5. get the end node, make it point to head

return newHead

RunTime : O(1)


"""


def rotate_list(head, k):
    #TODO: Write - Your - Code
    N = 0

    temp = head

    while temp:
        N+=1
        temp = temp.next

    n = k
    n = n % N

    if n < 0:
        n = n+N

    #positive K
    if True:
        n = N - n
        temp = head

        while n > 0:
            prev = temp
            temp = temp.next
            n-=1

        prev.next = None
        newHead = temp

        while temp.next:
            temp = temp.next

        temp.next = head
        return newHead
