class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
def insertNode(node, nodeData):
    if node is None:
        return Node(nodeData)
    if nodeData < node.data:
        node.left = insertNode(node.left, nodeData) # recursive it if left is None then create a new node with nodeData
    elif nodeData > node.data:
        node.right = insertNode(node.right, nodeData)
    return node

def minValueNode(node): #left tree will has the smallest value
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(node, key):
    if node is None :  #往下找 直到找不到 往回退
        return node
    if key < node.data: # find left tree
        node.left = deleteNode(node.left, key)
    elif key > node.data:
        node.right = deleteNode(node.right, key)

    # the key is same as node'root, this is the node need to delete
    else:
        if node.left is None:
            temp = node.right #sub right tree replace original node
            node.data = None
            return temp
        elif node.right is None:
            temp = node.left
            node.data = None
            return temp
        # right and left both have child
        # take right subtree's min to be the new node
        else:               
            temp = minValueNode(node.right) #can be the min value of right tree
                                            #or the max value of left tree
            #copy to this node (since it was removed)
            node.data = temp.data 
            # subtree's(node.right) min(temp.data) is deleted
            node.right = deleteNode(node.right, temp.data)
    return node

def printTree(node, mode):
    # left root right
    if mode == 'inorder':
        if node is not None:
            printTree(node.left,mode)
            print(node.data)
            printTree(node.right,mode)
    # root left right
    elif mode == 'preorder':
        if node is not None:
            print(node.data)
            printTree(node.left,mode)
            printTree(node.right,mode)
    # left right root 
    elif mode == 'postorder':
        if node is not None:
            printTree(node.left,mode)
            printTree(node.right,mode)
            print(node.data)

#       7
#     /  \
#     4   13
#   /  \
#   1
#     \
#      2





root = Node(7)
root = insertNode(root, 4)
root = insertNode(root, 1)
root = insertNode(root, 5)
root = insertNode(root, 2)
root = insertNode(root, 13)
printTree(root,'preorder')

# print('the tree:  ')
# printTree(root)
# tmp = root.left
# print('left tree: ')
# printTree(tmp)
# tmp = root.right
# print('right tree: ')
# printTree(tmp)
# print('-----delete-----')
# root = deleteNode(root,4)
# printTree(root)
# print('-----search-----')
# print(searchTree(root, 9))