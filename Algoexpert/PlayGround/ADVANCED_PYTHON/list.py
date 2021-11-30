# Using List as Stack
from collections import deque

def stack():
    stack = [1, 2, 3]
    stack.append(4)
    print(f"append {stack}")
    stack.pop()
    print(f"pop {stack}")
#stack()

def queue():
    q = deque([1, 2, 3])
    q.append(4)
    print(q)
    q.popleft()
    print(q)
    q.append(5)
    print(q)

queue()



