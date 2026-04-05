# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        SEEN_VALUE = -9999
        check = head

        while check is not None:
            if check.val == SEEN_VALUE:
                return True

            check.val = SEEN_VALUE
            check = check.next
        return False