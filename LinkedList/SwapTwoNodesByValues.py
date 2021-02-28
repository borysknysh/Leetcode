# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        curr = head
        
        while curr != None and curr.next != None:
            if curr.val != curr.next.val:
                temp = curr.val
                curr.val = curr.next.val
                curr.next.val = temp
            curr = curr.next.next
            
        return head
