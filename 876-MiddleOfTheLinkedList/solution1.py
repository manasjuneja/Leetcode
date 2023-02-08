# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        curs = head

        while curs != None and curs.next != None:
          cur = cur.next
          curs = curs.next.next

        return cur

