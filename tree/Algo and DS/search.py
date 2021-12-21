def searchTree(node, targetValue):
    if node is None:
        return ('empty tree')
    
    n = 1 #visit root need to count to 1
    while True:
        if node.data == targetValue:
            return ('search {0} times'.format(n))
        if targetValue < node.data: #search left
            node = node.left
        elif targetValue > node.data:
            node = node.right
        n += 1
# recursive
def searchTree_rec(node, targetValue):
    if node is None:
        print('No node found')
        return None
    if node.data == targetValue:
        print('Found node')
        return node
    elif node.data < targetValue:
        return searchTree_rec(node.right, targetValue)
    else:
        return searchTree_rec(node.left, targetValue)
