#112
def hasSum(node, targetSum, cur):
    if node is None:
        return False
    cur += node.val
    if cur == targetSum and cur.left is None and cur.right is None:
        return True
    return hasSum(node.left, targetSum, cur) or hasSum(node.right, targetSum, cur)
def hasPathSum(root, targetSum):
    return hasSum(root, targetSum, 0)

'''
TC is O(n), travel all nodes
SC is O(n), recursive nature of the solution
'''