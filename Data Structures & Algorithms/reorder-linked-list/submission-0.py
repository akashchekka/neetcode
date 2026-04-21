# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        stack = []
        while second:
            stack.append(second)
            second = second.next

        temp = head

        while stack:
            current = stack.pop()
            current.next = temp.next
            temp.next = current
            temp = temp.next.next