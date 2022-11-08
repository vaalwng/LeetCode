# create a class for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createCycle(head, tPos):
    temp = head
    count = 0

    # traverse to target position
    while count < tPos:
        temp = temp.next
        count = count + 1
    
    # create the join point
    join = temp

    # traverse to the end
    while temp.next != None:
        temp = temp.next
    
    # connect the end to the target position
    temp.next = join

    return head

# determines if a linked list has a cycle
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

# creates a linked list from an iterable
def createLinkedList(arr):
    head = ListNode(arr[0])
    for a in arr[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(a)
    return head

# creates a string from the linked list for printing
def linkedListToString(head):
    if hasCycle(head):
        return "ERROR (LinkedListToString()): Linked List contains a cycle!"
    else:
        s = "["
        if head.val != None:
            s = s + str(head.val)
            while head.next != None:
                s = s + " " + str(head.next.val)
                head = head.next
        s = s + "]"
        return s