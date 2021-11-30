# Traverse the tree in IN order
# Convert the Node to tail of Linked list
class CONVERT_BST_INTO_DLL:
    def __init__(self):
        self.value = None
        self.head = None
        self.tail = None

    def convertBinaryTreeToDoublyLinkedList(self, tree):
        currentNode = tree
        if currentNode is None:
            return
        self.convertBinaryTreeToDoublyLinkedList(currentNode.left)
        if self.head is None:
            self.head = self.tail = currentNode
        else:
            self.tail.right = currentNode
            currentNode.left = self.tail
            self.tail = currentNode
        self.convertBinaryTreeToDoublyLinkedList(currentNode.right)

    def printDLL(self):
        currentNode = self.head
        if currentNode:
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.right

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


    #Average O(log(n)) time | O(log(n)) space
    #Worst O(n) time | O(n) space

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True


    # Average O(log(n)) time | O(log(n)) space
    # Worst O(n) time | O(n) space
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parnetNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        #this is a single-node tree do nothing
                        pass
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
            return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value, end=',')
        if self.right:
            self.right.printTree()


    def getMin(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def getMax(self):
        currentNode = self
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.value

def getDepth(tree):
    currentNode = tree
    if currentNode is None:
        return 0
    leftDepth = getDepth(tree.left)
    rightDepth = getDepth(tree.left)

    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1

def inOrder(tree):
    if tree:
        inOrder(tree.left)
        print(tree.value, end=',')
        inOrder(tree.right)


def preOrder(tree):
    if tree:
        print(tree.value, end=',')
        preOrder(tree.left)
        preOrder(tree.right)

def postOrder(tree):
    if tree:
        postOrder(tree.left)
        postOrder(tree.right)
        print(tree.value, end=',')



root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
root.printTree()
print("\n Insert 12")
root.insert(12)
root.printTree()
print("\n Remove 10")
root.remove(10)
root.printTree()
print("\n Contains 10")
print(root.contains(10))
print("\n contains 5")
print(root.contains(5))
print("\n Tree Depth")
print(getDepth(root))
print(f"Inorder Traversal: ")
inOrder(root)
print(f"\nPreorder Traversal:")
preOrder(root)
print(f"\npostOrder Traversal:")
postOrder(root)

DLL = CONVERT_BST_INTO_DLL()
DLL.convertBinaryTreeToDoublyLinkedList(root)
print("\n Doubly linked list")
DLL.printDLL()
#root.remove(1)
#root.printTree()