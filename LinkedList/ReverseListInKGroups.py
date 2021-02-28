# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        temp = head
        for i in range(k):
            if not temp:
                return head
            temp = temp.next
        
        pre = None
        cur = head
        nex = None
        
        cntr = 0
        while cur and cntr < k:
            nex = cur.next
            cur.next = pre
            
            pre = cur
            cur = nex
                
            cntr += 1

        if nex:
            head.next = self.reverseKGroup(nex, k)
        
        return pre
