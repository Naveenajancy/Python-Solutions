def longestCommonPrefix(string):
    longestPrefix = " "
    if not string:
        return longestPrefix
    shortestString = min(string, key=len)
    for i in range(1, len(shortestString)):
        if all(x.startswith(shortestString[:i+1]) for x in string):
            longestPrefix = shortestString[:i+1]
        else:
            break
    return longestPrefix

print(longestCommonPrefix(["flower", "flow", "flight"]))