# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):234. Palindrome Linked List

#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        cur = head
        pre = None

        while cur:

            if cur.val == val:
                if pre:
                    pre.next = cur.next
                    cur = cur.next
                    continue
                elif not pre:
                    head = head.next
                    cur = cur.next
                    continue

            pre = cur
            cur = cur.next

        return head
