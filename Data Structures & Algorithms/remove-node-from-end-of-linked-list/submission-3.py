# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        L = dummy
        R = head

        for i in range(n):
            R = R.next

        while R:
            L = L.next
            R = R.next

        # Remove next node from L
        temp = L.next.next
        L.next = temp

        return dummy.next
