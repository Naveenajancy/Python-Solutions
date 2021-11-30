class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def printSinglyLinkedlist(self):
        datavalue = self.head
        while datavalue is not None:
            print(datavalue.value,"-> " ,end='')
            datavalue = datavalue.next

    def insertAtBegining(self, newvalue):
        if self.head is None:
            self.head = Node(newvalue)
        else:
            newNode = Node(newvalue)
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, newvalue):
        newNode = Node(newvalue)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode




list = SinglyLinkedList()
list.head = Node("Monday")
d2 = Node("Tuesday")
d3 = Node("wednessday")
d4 = Node("Thrusday")
#list.printSinglyLinkedlist()
list.head.next = d2
d2.next = d3
d3.next = d4
list.printSinglyLinkedlist()
list.insertAtBegining("Sunday")
#list.printSinglyLinkedlist()
list.insertAtEnd("Friday")
#list.printSinglyLinkedlist()