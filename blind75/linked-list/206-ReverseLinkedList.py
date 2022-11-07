# create a class for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None     

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

def linkedListToString(head):
    s = ""
    if head.val != None:
        s = s + str(head.val)
        while head.next != None:
            s = s + str(head.next.val)
            head = head.next
    
    return s

if __name__ == "__main__":

    # [1, 2, 3, 4]
    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(3)
    n1.next.next.next = ListNode(4)

    print(linkedListToString(n1))
    
    sum = reverseLinkedList(n1)
    print(linkedListToString(sum))