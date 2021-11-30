# O(n^2) time | O(1) Space
def twonumbersum(numarray, targetedsum):
    sortedlist = []
    if len(numarray) is 0:
        return []
    else:
        for i in range(len(numarray)):
            for j in range(i+1, len(numarray)):
                add = numarray[i] + numarray[j]
                if add == targetedsum:
                    numbers = numarray[i], numarray[j]
                    sortedlist.append(numbers)
                    #return numbers
        return sortedlist


#O(n) time | O(n) space

def twoNum(array, targetsum):
    nums = {}
    final = []
    for num in array:
        match = targetsum - num
        if match in nums:
            pair = [match, num]
            final.append(pair)
            #return final
        else:
            nums[num] = True
    return final

output = twonumbersum([12, 2, -2, 8, 5, 3, 4, 6], 10)
print(f"Two Num ")
print(twoNum([12,2,-2,8,5,4,3,2,1], 10))


#Leetcode timecomplexity less than O(n^2)
#Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# O(n) Time | O(n) the extra space required depends on the number of items stored in the hash table which stores exactly n elememts

def twoSums(array, target):
    diffMap = {}
    for idx, num in enumerate(array):
        diff = target - num
        print(f"diffMap {diffMap} , idx {idx}")
        if diff not in diffMap:
            diffMap[num] = idx
            print(f"n not in dict {diff} {diffMap}")
        else:
            return [diffMap[diff], idx]




print(twoSums([2, 7, 11, 15], 9))

print(twoSums([3, 2, 4], 6))


#print(twoSums([3, 3], 6))
