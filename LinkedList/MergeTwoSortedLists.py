# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addElement(self, l, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return self.head
        else:
            l.next = new_node
            return l.next
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.head = None        
        l = self.head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l = self.addElement(l,l1.val)
                l1 = l1.next
            else:
                l = self.addElement(l,l2.val)
                l2 = l2.next
        
        while l1 != None:
            l = self.addElement(l, l1.val)
            l1 = l1.next
            
        while l2 != None:
            l = self.addElement(l ,l2.val)
            l2 = l2.next

        return self.head
