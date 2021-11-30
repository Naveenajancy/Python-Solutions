#Remove Duplicates from array in place with O(1) memory space
#I think this moves the unique element i.e. nums[i] to its correct position i.e. the next duplicated element.
#Think of len_ as a pointer that keeps track of the index we should drop or place the next unqiue element
#and i as the pointer that iterates over the array and finds the next unique element.
#When we find the next unique element i.e. nums[i] != num[i-1], we place the unique element in the correct place i.e. nums[len_]
# Use In Interpreter Python automatically stores the value of the last expression in the interpreter
#to a particular variable called "_." You can also assign these value to another variable if you want

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                #print(f"num[len_] {nums[len_]} len_ {len_}")
                len_ +=1
        return len_

S = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 5]
len_ = S.removeDuplicates(nums)
#print(len_)
for i in range(len_):
    print(nums[i])
