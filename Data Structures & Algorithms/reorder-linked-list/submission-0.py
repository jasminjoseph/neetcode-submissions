# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        L = head
        R = head

        # Find middle of linked list
        while R and R.next:
            L = L.next
            R = R.next.next

        # Reverse second part
        prev = None
        curr = L.next
        L.next = None

        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Make reorder list
        second = prev
        first = head

        while first and second:
            firstTemp = first.next
            secondTemp = second.next

            first.next = second
            second.next = firstTemp

            first = firstTemp
            second = secondTemp


     





        