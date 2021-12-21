#101
# left subtree.left == right subtree.right
# left subtree.right == right subree.left
def isMirror(t1, t2):
    if(t1 is None and t2 is None):
        return True
    if (t1 is None or t2 is None):
        return False
    return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

def isSymmetric(root):
    isMirror(root, root)


'''
TC is O(n), visited all nodes
SC us O(n), recursion call stack
'''