# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(Nk) in time and O(1) space complecity solution 
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
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        
        total = lists[0]
        cntr = 0
        while cntr < length-1:
            total = self.merge2Lists(total, lists[cntr+1])
            cntr += 1
        
        return total
            
