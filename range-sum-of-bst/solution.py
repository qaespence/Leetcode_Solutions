# Definiton for a binary tree node.

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value)
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0
        if (not root):
            return 0
        if L <= root.data <= R:
            return root.data + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

test = Solution()

testTree = Tree()
testTree.addNode(testTree.root, 10)
testTree.addNode(testTree.root, 5)
testTree.addNode(testTree.root, 15)
testTree.addNode(testTree.root, 3)
testTree.addNode(testTree.root, 7)
testTree.addNode(testTree.root, 0)
testTree.addNode(testTree.root, 18)

print(test.rangeSumBST(testTree.root, 7, 15))

testTree2 = Tree()
testTree2.addNode(testTree2.root, 10)
testTree2.addNode(testTree2.root, 5)
testTree2.addNode(testTree2.root, 15)
testTree2.addNode(testTree2.root, 3)
testTree2.addNode(testTree2.root, 7)
testTree2.addNode(testTree2.root, 13)
testTree2.addNode(testTree2.root, 18)
testTree2.addNode(testTree2.root, 1)
testTree2.addNode(testTree2.root, 0)
testTree2.addNode(testTree2.root, 6)

print(test.rangeSumBST(testTree2.root, 6, 10))
