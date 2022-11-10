# LinkedList class definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def createCycle(self, targetPos):
        temp = self
        count = 0 

        # traverse to target position
        while count < targetPos:
            temp = temp.next
            count = count + 1
        
        # create the join point
        join = temp

        # traverse to the end
        while temp.next != None:
            temp = temp.next
        
        # connect the end to the target position
        temp.next = join

        return self

    # creates a string from the linked list for printing
    def linkedListToString(self):
        if self.hasCycle():
            return "ERROR (LinkedListToString()): Linked List contains a cycle!"
        else:
            s = "["
            if self.val != None:
                s = s + str(self.val)
                while self.next != None:
                    s = s + " " + str(self.next.val)
                    self = self.next
            s = s + "]"
            return s

    # determines if a linked list has a cycle
    def hasCycle(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        if self is None:
            return False

        slow = self
        fast = self

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