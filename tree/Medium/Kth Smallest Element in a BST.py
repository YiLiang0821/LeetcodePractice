#230
# inorder 
class Solution:
    def inorderSearch(self, root):
        # this is stop recursive consition, it's a must!
        if root is None:
            return
        self.inorderSearch(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return 
        self.inorderSearch(root.right)
        
    def kthSmallest(self, root, k: int) -> int:
        self.k = k
        self.ans = None
        self.inorderSearch(root)
        return self.ans
'''
TC is O(n), we will touch every nodes in worst case
SC is O(n) due to use recursive to call stack
'''