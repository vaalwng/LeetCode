# BinaryTree class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, data):
        if self.val:
            # data LESS THAN current node value
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
        
    def printTreeInOrder(self):       
        if self.left:
            self.left.printTreeInOrder()
        print(self.val)
        if self.right:
            self.right.printTreeInOrder()

    def printTreePreOrder(self):  
        print(self.val)
        if self.left:
            self.left.printTreePreOrder()
        if self.right:
            self.right.printTreePreOrder()
    
    def printTreePostOrder(self):  
        if self.left:
            self.left.printTreePostOrder()
        if self.right:
            self.right.printTreePostOrder()
        print(self.val)