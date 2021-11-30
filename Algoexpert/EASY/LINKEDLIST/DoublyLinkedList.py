# 1. Contains node with N value
# 2. remove method

class Node:
   def __init__(self, value):
       self.value = value
       self.prev = None
       self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) | Time - O(1) | Space

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    # O(1) - Time and space

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBinding(node)

    def removeNodeBinding(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # O(1) Time and Space

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        #nodeToInsert = Node(nodeToInsert)
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    #O(1) Time | O(1) Space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        #nodeToInsert = Node(nodeToInsert)
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(p) time | O(1) space

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertAfter(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(1) time | O(1) space

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) Time and Space

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def printList(self):
        node = self.head
        while node is not None:
            print(node.value, "->", end='')
            node = node.next




Dll = DoublyLinkedList()
one = Node(10)
two = Node(20)
three = Node(30)
three2 = Node(30)
three3 = Node(30)
four = Node(40)
five = Node(50)
six = Node(60)
Dll.printList()
Dll.setHead(one)
Dll.setTail(six)
Dll.insertAfter(one, two)
Dll.insertAfter(two, three)
Dll.insertBefore(three, four)
Dll.insertAfter(six, five)
Dll.insertAtPosition(1, three2)
Dll.insertAfter(six, three3)
Dll.printList()
Dll.removeNodesWithValue(30)
print("after removing nodes 30 \n")
Dll.printList()
print("Remove 20 \n")
Dll.remove(two)
Dll.printList()



