from BinaryTreeImpl import TreeNode

def maxTreeDepth(root):
    """
    :type root:TreeNode
    :rtype: int
    """
    # recursive approach
    if not root:
        return 0
    
    return 1 + max(maxTreeDepth(root.left), maxTreeDepth(root.right))

    # iterative approach
    # if not root:
    #     return 0
    
    # stack = [(root, 1)]
    # maxDepth = 1

    # while stack:
    #     node, depth = stack.pop()
    #     maxDepth = max(maxDepth, depth)

    #     if node.left:
    #         stack.append((node.left, depth+1))
    #     if node.right:
    #         stack.append((node.right, depth+1))
        
    # return maxDepth


if __name__ == "__main__":
    tr = TreeNode(3)
    tr.left = TreeNode(9)
    tr.right = TreeNode(20)
    tr.left.left = None
    tr.left.right = None
    tr.right.left = TreeNode(15)
    tr.right.right = TreeNode(7)
    # tr.printTreeInOrder()
    print(maxTreeDepth(tr))

    tr2 = TreeNode(1)
    tr2.left = None
    tr2.right = TreeNode(2)
    # tr2.printTreeInOrder()
    print(maxTreeDepth(tr2))