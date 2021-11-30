#Construct stack with special operation MINMAX Stack - LIFO
# O(1) - Time | O(1) - Space

class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def push(self, number):
        newMinMax = {"min":number, "max":number}
        if (len(self.minMaxStack)):
            lastMinMaxValue = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMaxValue["min"], number)
            newMinMax["max"] = max(lastMinMaxValue["max"], number)
        self.minMaxStack.append(newMinMax)
        print(self.minMaxStack)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1] ["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1] ["max"]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def print(self):
        for elements in self.stack:
            print(elements)

S = MinMaxStack()
print("Pushing elemnts 10-14")
for x in range(10, 15):
    S.push(x)

S.push(1)
S.print()
P1 = S.pop()
print(f"pop P1 {P1}")
print(f"Get min {S.getMin()}")
print(f"get max {S.getMax()}")
S.print()
print(f"Pop {S.pop()}")
print(f"Get min {S.getMin()}")
print(f"get max {S.getMax()}")
print(f"Peek {S.peek()}")


