#141
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h = head
        t = head

        while t and h and h.next:
            t = t.next
            h = h.next.next
            if (t == h):
                return True
        return False


'''
Use Floyd's Algorithm (Tortoise and Hare Algorithm)
TC is O(n)
SC is O(1) only use two pointers
'''