#2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        pointer = ans
        sumDigits = 0
        carry = 0
        while(l1 or l2):
            sumDigits = carry   # 0 or 1
            if l1:
                sumDigits += l1.val
                l1 = l1.next
            if l2:
                sumDigits += l2.val
                l2 = l2.next
            carry = int(sumDigits // 10)
            pointer.next = ListNode(sumDigits % 10)
            pointer = pointer.next
        # check overflow
        if carry:
            pointer.next = ListNode(carry)

        return ans.next
'''
TC is O(n) -> n is the size of biggest linked list
SC is O(n)
'''