#124
class Solution:
    
    def count(self, node):
        if node is None:
            return 0
        left = self.count(node.left)
        right = self.count(node.right)
        
        maxSide = max(node.val, max(left, right) + node.val)
        maxTop = max(maxSide, node.val + left + right)
        self.ans = max(self.ans, maxTop)
        return maxSide
    def maxPathSum(self, root) -> int: 
        self.ans = -float('inf')
        self.count(root)
        return self.ans