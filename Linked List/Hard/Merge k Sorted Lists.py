#23
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeList(self, l1, l2):
    dummyNode = ListNode()
    ans = dummyNode
    while(l1 and l2):
        if (l1.val >= l2.val):
            dummyNode.next = l2
            l2 = l2.next
        else:
            dummyNode.next = l1
            l1 = l1.next
        dummyNode = dummyNode.next
    if (l1):
        dummyNode.next = l1
    if (l2):
        dummyNode.next = l2
    return ans.next


def mergeKLists(lists):
    if len(lists) == 0:
        return None
    '''
    solution 2 
    while(len(lists) > 1):
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeList(l1, l2))
            lists = merged 
    '''
    # head and tail meage
    l = 0
    r = len(lists) - 1
    last = r
    while(last != 0):
        l = 0
        r = last
        while (l < r):
            lists[l] = self.mergeList(lists[l], lists[r])
            l += 1
            r -= 1
            last = r
    return lists[0]

'''
TC is O(n log k), 
n is the nodes which every time merge two list take O(n), 
k is the k linked list
brust force is O(nk)
'''