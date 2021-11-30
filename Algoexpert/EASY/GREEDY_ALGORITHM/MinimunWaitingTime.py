def minimumWaitingTime(queries):
    queries.sort()
    queryTime = 0
    for i in range(1, len(queries)):
        while i > 0:
            #print(f"i {i} querytime B : {queryTime}")
            queryTime += queries[i - 1]
            i -= 1
            print(f"i - 1 : {i}, querytime A {queryTime}")
    return queryTime


def minwaittime(queries):

