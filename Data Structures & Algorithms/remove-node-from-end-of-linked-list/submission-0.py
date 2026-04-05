# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        
        loop = head
        while loop is not None:
            length += 1
            loop = loop.next
        
        idx = length - n
        loop = head
        prev = None
        for i in range(length):
            if i == idx:
                next_node = loop.next
                if next_node is None and prev is None:
                    return None
                elif next_node is None:
                    prev.next = None
                    return head
                elif prev is None:
                    return head.next
                else:
                    prev.next = next_node
                    return head
            else:
                prev = loop
                loop = loop.next

        return head