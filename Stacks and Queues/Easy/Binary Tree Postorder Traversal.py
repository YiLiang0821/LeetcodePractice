#145
# recursive version
def dfs(self,node):
    if node is None:
        return
    self.dfs(node.left)
    self.dfs(node.right)
    self.ans.append(node.val)
def postorderTraversal(self, root):
    self.ans = []
    self.dfs(root)
    return self.ans


from collections import deque
def postorderTraversal_nonRec(self, root) :
        order = deque()
        stack = [root]
        while(stack):
            node = stack.pop()
            order.appendleft(node.val)
            # not None
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return order
'''
append order: mid, right, left
due to stack, append left then right
TC is O(n), n is nodes of Tree
SC is O(n), stack(n) and queue(n) 
'''