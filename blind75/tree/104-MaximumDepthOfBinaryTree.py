from TreeImpl import TreeNode
from TreeImpl import printTree
from TreeImpl import insertToTree

def maxTreeDepth(root):
    """
    :type root:TreeNode
    :rtype: int
    """
    # recursive approach
    if not root:
        return 0
    
    return 1 + max( root.maxTreeDepth(root.left), root.maxTreeDepth(root.right) )

if __name__ == "__main__":
    tr = TreeNode(3)
    tr.left = TreeNode(9)
    tr.right = TreeNode(20)
    tr.right.left = TreeNode(15)
    tr.right.right = TreeNode(7)

    tr2 = TreeNode(3)
    tr22 = insertToTree(tr2, 9)

    print(printTree(tr))
    # print(maxTreeDepth())