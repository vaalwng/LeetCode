from LinkedListImpl import ListNode
from LinkedListImpl import createLinkedList

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
    print(l.linkedListToString())
    print(l.hasCycle())
    c = l.createCycle(1)
    print(l.hasCycle())