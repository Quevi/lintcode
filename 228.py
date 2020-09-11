# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while True:
            fast = fast.next
            if fast is None:
                return slow.next
            fast = fast.next
            if fast is None:
                return slow.next
            slow = slow.next

