# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(N*logk) time complecity and O(1) space complecity
class Solution:
    def merge2Lists(self, l1, l2):
        head = temp = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
            
        return head.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        gap = 1
        while gap < length:
            for cntr in range(0, length-gap, 2*gap):
                lists[cntr] = self.merge2Lists(lists[cntr], lists[cntr+gap])
            gap *= 2
        
        return lists[0] if length > 0 else None
