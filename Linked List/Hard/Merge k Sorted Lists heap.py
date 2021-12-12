#23
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if len(lists) == 0:
        return None
    h = []
    # push first round values into heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, [lists[i].val, i]) # push the index(index of lists) and the vaule
            lists[i] = lists[i].next
    head = ListNode()
    pointer = head
    while(h):
        v, i = heapq.heappop(h)
        pointer.next = ListNode(v)
        pointer = pointer.next
        if lists[i]:
            heapq.heappush(h, [lists[i].val, i])
            lists[i] = lists[i].next
    return head.next
'''
heapq.heappush will use first elements to order the queue.
queue size will k, every time heap order take O(log k)
TC is O(n log k), n is the longest subList of lists
SC is O(k)
'''
    