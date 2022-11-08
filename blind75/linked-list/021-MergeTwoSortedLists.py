from LinkedListImpl import ListNode
from LinkedListImpl import createLinkedList
from LinkedListImpl import linkedListToString

def mergeTwoSortedLists(list1, list2):
    """
    :type list1: ListNode
    :type list2: ListNode
    :rtype ListNode
    """
    
    # validate lists
    if list1 is None or list2 is None:
        return None
    
    # identify which head is smaller
    if list1.val < list2.val:
        temp = head = ListNode(list1.val)
        list1 = list1.next
    else:
        temp = head = ListNode(list2.val)
        list2 = l2.next

    # loop until either of the lists are NULL
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            temp.next = ListNode(list1.val)
            list1 = list1.next
        else:
            temp.next = ListNode(list2.val)
            list2 = list2.next
        temp = temp.next
    
    # add all the nodes in list1, if remaining
    while list1 is not None:
        temp.next = ListNode(list1.val)
        list1 = list1.next
        temp = temp.next
    
    # add all the nodes in list2, if remaining
    while list2 is not None:
        temp.next = ListNode(list2.val)
        list2 = list2.next
        temp = temp.next
    
    return head

if __name__ == "__main__":
    arr1 = [1,4,6]
    arr2 = [3,5,7]
    l1 = createLinkedList(arr1)
    l2 = createLinkedList(arr2)
    print(linkedListToString(l1))
    print(linkedListToString(l2))

    sortedList = mergeTwoSortedLists(l1, l2)
    print(linkedListToString(sortedList))
