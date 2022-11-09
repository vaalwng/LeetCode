# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertToTree(root, val):
    if val < root.val:
        if root.leftChild:
            root.leftChild.insert(val)
        else:
            root.leftChild = TreeNode(val)
            return
    else:
        if root.rightChild:
            root.rightChild.insert(val)
        else:
            root.rightChild = TreeNode(val)
            return

def printTree(root):
    if root.left:
        printTree(root.left)

    print(root.val)

    if root.right:
        printTree(root.right)