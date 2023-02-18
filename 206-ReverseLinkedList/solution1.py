# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        a = []

        while cur :
            a.append(cur.val)
            cur = cur.next

        a = a[::-1]

        if len(a) == 0:
            return None

        start = ListNode(a[0])
        cur_node = start

        for i in a[1:] :
            new_node = ListNode(i)
            cur_node.next = new_node
            cur_node = new_node

        cur_node.next = None

        return start
