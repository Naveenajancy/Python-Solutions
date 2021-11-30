class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# O(n) time | O(d) space
def invertBinaryTree(tree):
    if tree is None:
        return
    swapTreeElements(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapTreeElements(tree):
    tree.left, tree.right = tree.right, tree.left

# Breadth First Search algorithm
#O(n) time | O(n)
def ibtIterative(tree):
    queue = [tree]
    while len(queue)
        currentNode = queue.pop(0)
        if currentNode is None:
            return
        swapTreeElements(currentNode)
        queue.append(currentNode.left)
        queue.append(currentNode.right)





