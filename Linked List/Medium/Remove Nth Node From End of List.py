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
L 和 R 相差n , 當 R == False 時，L 會在要移除點的前一個
TC is O(2*n) = O(n)
SC is O(1) only two pointers
'''