# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(0)

        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next

        l3.next = l1 or l2
        return head.next

    def mergeTwoLists1(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = mergeTwoLists1(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists1(l1, l2.next)
            return l2
