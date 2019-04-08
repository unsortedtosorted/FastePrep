"""
1. create a new list
2. delete head of old list and keep adding it to front of new list
3. decrement k
4. when k = 0
5. assign tail.next to head of remaining old list
6. return newHead

Runtime : O(N)
Memory : O(1)


""""



def reverse_k_nodes(head, k):
    if not head or not head.next or k == 0:
      return head


    tail = head
    head = head.next
    newHead = tail
    tail.next = None

    k-=1

    while k > 0:

        if not head:
            return None

        temp = head

        #delete node from old list
        head = head.next

        #add new node to in from of tail
        temp.next = newHead
        newHead = temp

        k-=1

    tail.next = head

    return newHead
