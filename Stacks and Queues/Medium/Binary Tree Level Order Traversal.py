#102
# BFS, use queue
from collections import deque
# use list with pop(0) also can remove first element
def levelOrder(root):
    ans = []
    if root is None:
        return ans
    q = deque([root])
    while(q):
        temp = []
        for _ in range(len(q)):
            node = q.popleft()
            temp.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        if len(temp) > 0:           
            ans.append(temp[:]) # [:] will generate a new list then append to ans
            temp.clear()
    return ans