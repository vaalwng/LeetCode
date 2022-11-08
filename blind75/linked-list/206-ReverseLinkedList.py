from LinkedListImpl import ListNode
from LinkedListImpl import createLinkedList
from LinkedListImpl import linkedListToString

def reverseLinkedList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # O(n)

    # declare prev and current ListNodes
    prev = None
    curr = head

    # iterate through linked list
    while curr: 

        # swap directions
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev

if __name__ == "__main__":

    arr = [1,2,3,4,5]
    l = createLinkedList(arr)
    print(linkedListToString(l))
    rL = reverseLinkedList(l)
    print(linkedListToString(rL))