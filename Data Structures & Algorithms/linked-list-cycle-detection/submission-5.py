# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        hasCycle = False

        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    hasCycle = True
                    break
            except:
                break
        
        return hasCycle
        

