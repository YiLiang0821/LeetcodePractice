#103
#BFS odd: left to right; even: right to left
from collections import deque
def zigzagLevelOrder(root):
    ans = []
    if root is None:
        return ans
    q = deque([root])
    tag = 1
    while (q):
        temp = []
        for _ in range(len(q)):
            if tag % 2 == 1:
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            else:
                node = q.pop()
                if node.right is not None:
                    q.appendleft(node.right)
                if node.left is not None:
                    q.appendleft(node.left)
                
            temp.append(node.val)
        if len(temp) > 0:
            ans.append(temp[:])
            temp.clear()
        tag += 1
    return ans
        