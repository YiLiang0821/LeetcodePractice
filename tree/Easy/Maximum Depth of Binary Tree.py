#104
# recursive
# every node check left and right
# if None(not exist) return 0, if till leaf node return 1
def maxDepth(root):
    if root is None:
        return 0
    # leaf node
    if root.left is None and root.right is None:
        return 1
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1
'''
TC is O(n), travel all of nodes
SC is O(h), h is the height of the tree
'''