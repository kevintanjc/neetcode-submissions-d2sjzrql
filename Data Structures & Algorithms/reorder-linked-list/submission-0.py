# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def getNodeAtIndex(head, index, total):
            i = 0
            link = head
            for i in range(total):
                if i == index:
                    return link
                else:
                    link = link.next
            return link

        length = 0
        check = head
        while check is not None:
            length += 1
            check = check.next
        
        next = None
        index = length - 1
        ptr = head
        for i in range(length // 2):
            next = ptr.next
            link = getNodeAtIndex(head, index, length)
            ptr.next = link
            ptr = link
            ptr.next = next
            ptr = ptr.next
            
        ptr.next = None
