#297

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # basic case
        # if None -> X, # is sperator
        # preoder: mid, left, right
        if root is None:
            return 'X#'
        leftSerialize = self.serialize(root.left)
        rightSerialize = self.serialize(root.right)
        final = str(root.val)+'#'+ leftSerialize + rightSerialize
        return final
        

    def deserialize(self, data):
        # remove sperator # first
        def recNode():
            # queue pop out first
            val = next(data)
            if val == 'X':
                return None
            # generate tree node, follow preorder
            node = TreeNode(int(val))
            node.left = recNode()
            node.right = recNode()
            return node

        data = iter(data.split('#'))
        return recNode()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
'''
serialize
 - TC is O(n), travel all nodes
 - SC is O(n), due to recursive to call a stack
deserialize
 - TC is O(n), travel all nodes
 - SC is O(n), due to recursive to call a stack
'''