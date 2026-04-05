# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def link(tail, head1, head2):
            if head1 is None and head2 is None:
                return
            elif head1 is None:
                tail.next = head2
                return
            elif head2 is None:
                tail.next = head1
            else:
                if head1.val < head2.val:
                    tail.next = head1
                    tail = head1
                    head1 = head1.next
                    return link(tail, head1, head2)
                else:
                    tail.next = head2
                    tail = head2
                    head2 = head2.next
                    return link(tail, head1, head2)
            
        if list1 is None and list2 is None:
            return None
        elif list2 is None:
            return list1
        elif list1 is None:
            return list2
        else:
            head = None

            if list1.val < list2.val:
                head = list1
                link(head, list1.next, list2)
            else:
                head = list2
                link(head, list1, list2.next)
            
            return head


        
