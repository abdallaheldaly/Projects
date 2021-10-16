# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        head1 = dummy
        
        for i in range(left - 1):
            head1 = head1.next
        p = head1.next
        
        for i in range(right - left):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
            
        return dummy.next
 
