# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()

        while head is not None:
            output.val = head.val
            link = ListNode()
            link.next = output
            output = link
            head = head.next

        return output.next
            