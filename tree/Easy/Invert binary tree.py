#226
def invertTree(root):
    if root:
        root.right, root.left = root.left, root.right
        invertTree(root.right)
        invertTree(root.left)
    return root