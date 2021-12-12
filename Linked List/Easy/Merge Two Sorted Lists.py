#21
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) -> ListNode:
        curr = ListNode()
        ans = curr
        while(list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # check remain list
        while(list1):
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        while(list2):
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return ans.next

list1 = [1,2,4]
list2 = [1,3,4]
solution = Solution()
print(solution.mergeTwoLists(list1, list2))

'''
TC is O(n)
SC is O(1)
'''