from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def AddTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = None
    temp = None
    carry = 0

    while l1 is not None or l2 is not None:
        sum_value = carry

        if l1 is not None:
            sum_value += l1.val
            l1 = l1.next
        if l2 is not None:
            sum_value += l2.val
            l2 = l2.next
        
        node = ListNode(sum_value % 10)
        carry = sum_value // 10

        if temp is None:
            temp = head = node
        else:
            temp.next = node
            temp = temp.next
    
    if carry > 0:
        temp.next = ListNode(carry)

    return head


if __name__ == "__main__":
    n1 = ListNode(2)
    n1.next = ListNode(4)
    n1.next.next = ListNode(3)

    n2 = ListNode(5)
    n2.next = ListNode(6)
    n2.next.next = ListNode(4)

    print(AddTwoNumbers(n1, n2).val, AddTwoNumbers(n1, n2).next.val, AddTwoNumbers(n1, n2).next.next.val)