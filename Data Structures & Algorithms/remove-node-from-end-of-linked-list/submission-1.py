# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
            
        temp = head
        l = 0

        while temp:
            l += 1
            temp = temp.next

        c = l - n

        if c == 0:
            return head.next

        temp = head
        while c - 1 > 0 and temp:
            temp = temp.next
            c -= 1

        if temp and temp.next:
            temp.next = temp.next.next

        return head
