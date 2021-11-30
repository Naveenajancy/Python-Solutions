class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        currentValue = self.head
        while (currentValue):
            print(currentValue.value)
            currentValue = currentValue.next

#LIFO Queue Push
#push (insert in the beginning)
# pop delete the first node

    def insertAtBeginning(self, newValue):
        if self.head is None:
            self.head = newValue
            return
        newNode = Node(newValue)
        newNode.next = self.head
        self.head = newNode

    def isempty(self):
        return True if self.head == None else False

    def pop(self):
        if self.isempty():
            return None
        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.value



    def insertAtEnd(self, newValue):
        if self.head is None:
            self.head = newValue
            return

        else:
            currentValue = self.head
            while currentValue.next is not None:
                currentValue = currentValue.next
            currentValue.next = Node(newValue)

#insert node inbetween
    def insertInbetween(self, previousNode, newValue):
        if previousNode is None:
            return "The PreviousNode is absent"
        else:
            newNode = Node(newValue)
            newNode.next = previousNode.next
            previousNode.next = newNode


'''
list1 = LINKEDLIST()
list1.insertAtBeginning("January")
print(list1.head)
list1.printLinkedList()

'''

llist = LinkedList()
llist.head = Node("Monday")
n2 = Node("Tuesday")
n3 = Node("Wednessday")
#Link first node to second
llist.head.next = n2
#linke second node to third
n2.next = n3
n4 = llist.insertAtBeginning("January")
n5 = llist.insertAtEnd("December")
llist.insertInbetween(n2, "Thursday")
llist.printLinkedList()
print(f"popped node is : {llist.pop()}")
print(f"popped node is : {llist.pop()}")
print(f"popped node is : {llist.pop()}")
llist.printLinkedList()


