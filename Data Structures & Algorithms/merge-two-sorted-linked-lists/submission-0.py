# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        t1, t2 = list1, list2
        t3 = dummy
        while t1 and t2:
            if t1.val <= t2.val:
                t3.next = t1
                t1 = t1.next
            else:
                t3.next = t2
                t2 = t2.next
            t3 = t3.next

        if t1:
            t3.next = t1
        if t2:
            t3.next = t2

        return dummy.next