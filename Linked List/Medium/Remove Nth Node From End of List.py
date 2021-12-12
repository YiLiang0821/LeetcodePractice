#19
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        startNode = ListNode(0, head)
        L = startNode
        R = head
        # keep R - L = n
        while n > 0 and R:
            R = R.next
            n -= 1
        while R:
            L = L.next
            R = R.next
        L.next = L.next.next
        return startNode.next
'''
TC is O(2*n) = O(n)
SC is O(1) only two pointers
'''