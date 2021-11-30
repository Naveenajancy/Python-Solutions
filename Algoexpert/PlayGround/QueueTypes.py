# q in Python can be implemented by the following ways: #list #collections.deque #q.q
"""
Implementation using list
List is a Python’s built-in data structure that can be used as a q.
 Instead of enq() and deq(), append() and pop() function is used.
 However, lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring O(n) time.


Implementation using collections.deque
q in Python can be implemented using deque class from the collections module.
Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
Instead of enq and deque, append() and popleft() functions are used.

Implementation using q.q
q is built-in module of Python which is used to implement a q. q.q(maxsize) initializes a variable to a maximum size of maxsize.
A maxsize of zero ‘0’ means a infinite q. This q follows FIFO rule.
"""


from collections import deque
from queue import Queue

#q = []
q = deque()
for i in range(97, 123):
    q.append(chr(i))

print(f"q Values {q}")

for i in range(10):
    #print(q.pop(0))
    q.popleft()

print(f"q Values {q}")


"""
    maxsize – Number of items allowed in the q.
    empty() – Return True if the q is empty, False otherwise.
    full() – Return True if there are maxsize items in the q. If the q was initialized with maxsize=0 (the default), then full() never returns True.
    get() – Remove and return an item from the q. If q is empty, wait until an item is available.
    get_nowait() – Return an item if one is immediately available, else raise qEmpty.
    put(item) – Put an item into the q. If the q is full, wait until a free slot is available before adding the item.
    put_nowait(item) – Put an item into the q without blocking. If no free slot is immediately available, raise qFull.
    qsize() – Return the number of items in the q.
"""

q1 = Queue(maxsize = 10)
print(f"Queue Size {q1.qsize()}")

for i in range(10):
    q1.put(i)

print(f"Q elements are {q1.queue}")

print(f"Queue is full ? {q1.full()}")
for i in range(5):
    print(q1.get())

print(f"Is Q empty {q1.empty()}")


