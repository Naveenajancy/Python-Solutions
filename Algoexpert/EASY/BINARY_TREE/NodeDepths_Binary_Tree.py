class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right  = None


def nodeDepths(root, depth=0):
    if root is None:
        print(f"Root is None")
        return 0
    #return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

    #print(f"depth  {depth}")
    leftLevel = nodeDepths(root.left, depth + 1)
    #print (f"left level {leftLevel}")
    rightLevel = nodeDepths(root.right, depth + 1)
    #print(f"right level  {rightLevel}")
    print (f" d : {depth} LL : {leftLevel} RL: {rightLevel}")
    return depth + leftLevel + rightLevel

def printNodes(tree):
    if tree != None:

        printNodes(tree.left )#, level + 1)
        print(tree.value)
        printNodes(tree.right)#, level + 1)



root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
#root.left.right.left = BinaryTree(10)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
print(nodeDepths(root, depth=0))
print("Tree nodes")
printNodes(root)
