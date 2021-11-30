def solution(number):
    multiples = []
    for each in number:
        #print(f"numbers are {each} ")
        if each < 0:
            return 0
        elif ((each % 3 == 0) or (each % 5 == 0)):
            multiples.append(each)
            #print(f"number {each}")
        #else:
        #    print(f"multiples{multiples}")
    print(f"Final list {multiples}")
    return (sum(multiples))

a =solution([3,4,5,6,7,8,9])

#print(a)


def fizz_buzz(num):


fizz_buzz(9)