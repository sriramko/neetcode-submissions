# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        slow = head
        fast = head.next
        while True:
            if fast == slow:
                if fast.next:
                    return True
                else: return False
            if slow.next:
                slow = slow.next
            if fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
            
