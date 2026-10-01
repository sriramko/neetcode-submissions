# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return None
        one = l1
        two = l2
        currNode = ListNode()
        sumList = currNode
        carry = 0 # either 0 or 1 at all times
        while True:
            firstval = secondval = 0
            if one:
                firstval = one.val
            if two:
                secondval = two.val
            total = firstval + secondval
            total += carry # from previous place
            remainder = int(total % 10)
            currNode.val = remainder 
            carry = int(total / 10)
            if one:
                one = one.next
            if two:
                two = two.next
            if not one and not two and carry == 0:
                break
            nextNode = ListNode()
            currNode.next = nextNode
            currNode = nextNode
        return sumList
