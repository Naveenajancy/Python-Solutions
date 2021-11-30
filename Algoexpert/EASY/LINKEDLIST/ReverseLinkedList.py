class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value , "->", end='')
            currentNode = currentNode.next

# O(N) where N is the Number of nodes (length of linked list) storing three variables O(3) -> O(1)
    def reverseLinkedList(self):
        previousNode = None
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode





list = LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
list.printList()
print("\n reversing")
list.reverseLinkedList()
list.printList()

