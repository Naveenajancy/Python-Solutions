# Time - O(2^n)
# Space - O(n)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#print(fib(3))


def getNthFib(n , memoize={1:0, 2:1}):
    #print(type(memoize))
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        print(f"memoize[n] : {memoize[n]}")
        return memoize[n]

memoize = {1:0, 2:1}
n = 10
getFib = getNthFib(n, memoize)
print(f"{n} th fib number is {getFib}")





