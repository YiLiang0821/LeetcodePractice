#236

def lowestCommonAncestor(root, p, q):
    # basic case
    if root is None:
        return None
    if root.val == p.val or root.val == q.val:
        return root

    # recursive
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # check condition
    if (left is None and right is None):
        return None
    elif (left is not None and right is not None):
        return root
    elif left is None:
        return right
    else:
        return left


'''
TC is O(n) , search all nodes
SC is O(n) , will recursive all nodes, each take one space
'''