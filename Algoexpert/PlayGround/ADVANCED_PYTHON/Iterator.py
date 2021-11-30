# Iterator
class Counter:
    def __init__(self, low, high):
        print(f"low {low} -1 {low-1}")
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration

for c in Counter(3, 9):
    print(c)

# Generator

def counter(low, high):
    current =  low
    while current < high:
        yield current
        current += 1
for c in counter(3, 9):
    print(c)

