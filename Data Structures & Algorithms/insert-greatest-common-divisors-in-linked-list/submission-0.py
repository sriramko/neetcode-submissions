# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(a: int, b: int) -> int:
            while b > 0:
                a, b = b, a % b 
            return a
        if not head:
            return head

        curr = head
        while curr.next:
            n1, n2 = curr.val, curr.next.val
            insert = ListNode(GCD(n1, n2), curr.next)
            curr.next = insert
            curr = curr.next.next
        return head