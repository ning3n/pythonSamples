class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

DELIMITER = '#'

class Codec:

    def serialize(self, root):
        if not root:
            return ''
        
        def traverse(node):
            if node:
                temp_vals.append(str(node.val))
                traverse(node.left)
                traverse(node.right)
            else:
                temp_vals.append(DELIMITER)
        
        temp_vals = []
        traverse(root)
        return ' '.join(temp_vals)

    def deserialize(self,data):
        def build():
            val = next(temp_vals)
            if val == DELIMITER:
                return None
            node = Node(int(val))
            node.left = build()
            node.right = build()
            return node

        temp_vals = iter(data.split(''))
        return build()
