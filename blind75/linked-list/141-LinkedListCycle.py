from LinkedListImpl import ListNode
from LinkedListImpl import createLinkedList
from LinkedListImpl import linkedListToString
from LinkedListImpl import createCycle

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            return True
    
    return False

if __name__ == "__main__":
    arr = [3,2,0,-4]
    l = createLinkedList(arr)
    print(arr)
    print(linkedListToString(l))
    print(hasCycle(l))
    c = createCycle(l, 1)
    print(hasCycle(c))