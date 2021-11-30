#O(n) time O(1) Space
# you may say its runs O(n2) but its runs O(n) because we never consider the same elements more than one time.
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
        node = self.head
        while node:
            print(node.value, end = '->')
            node = node.next

    def insertatEnd(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            return
        lastnode = self.head
        #print(f"{lastnode.next} {lastnode.value}")
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode


    def sizeOfLinkedList(self):
        counter = 0
        currentNode = self.head
        while currentNode:
            currentNode = currentNode.next
            counter += 1
        return counter

    def removekNode(self, value):
        if self.head is None:
            return
        currentNode = self.head
        if currentNode.value == value:
            self.head = currentNode.next
            #currentNode = None
            return
        else:
            while currentNode:
                previousNode = currentNode
                currentNode = currentNode.next
                if currentNode.value == value:
                    previousNode.next = currentNode.next
                    return
                currentNode = currentNode.next

    def insertAtPosition(self):
        pass


    def removeDuplicatesFromLinkedlist(self):
        currentNode = self.head
        #print(currentNode.value)
        while currentNode is not None:
            nextDistinctNode = currentNode.next
            while nextDistinctNode is not None and currentNode.value == nextDistinctNode.value:
                nextDistinctNode = nextDistinctNode.next

            currentNode.next = nextDistinctNode
            currentNode = nextDistinctNode

        return self


l = LinkedList()
#l.head = Node(10)
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
print("linked list elements \n")
l.insertatEnd(100)
l.printList()
print(f"\n size of ll {l.sizeOfLinkedList()}")
l.removekNode(100)
print("\n Remove 100")
l.printList()
l.removekNode(20)
print("\n remove 20")
l.printList()
l.removekNode(40)
print("\n remove 40")
l.printList()
l.removekNode(50)
print("\n remove 50")
l.printList()
#l.removeDuplicatesFromLinkedlist()
#print("Distinct nodes \n")
#l.printList()
#print(f"size of ll {l.sizeOfLinkedList()}")
#llist.removeDuplicatesFromLinkedlist(sortedlinkedList)



