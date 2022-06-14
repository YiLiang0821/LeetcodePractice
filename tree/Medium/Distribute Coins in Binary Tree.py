# 979
# Tree, DP 
# balanced left subTree and right subTree
class Solution:
    def reBalance(self, node):
        if not node:
            return 0
        left = self.reBalance(node.left)
        right = self.reBalance(node.right)
        self.ans = self.ans + abs(left) + abs(right)
        return node.val - 1 + left + right
        
    def distributeCoins(self, root) -> int:
        self.root = root
        self.ans = 0
        self.reBalance(self.root)
        return self.ans
'''
node.val - 1(root self) + left + right
if 左子, 右子樹都balance, 當node = 1, root 本身也有coin了 -> 全部都balance (題目有說n coin with n nodes)
root = 0, 會變成 -1 -> 代表需要向root's parent 拿one coin
TC is O(n)
SC is O(n)
'''