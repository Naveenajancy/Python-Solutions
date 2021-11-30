#Given signed 32 - bit integer x,return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.
# Assume the  environment does not allow you to store 64 - bit integers(signed or unsigned).
# example 1:
# Input: x = 123
# Output: 321
# Input: x = -123
# Output: -321
# Input: x = 120
# Output: 21

class Solution:

    def reverseInteger(self, number):
        reverseNumber = (str(abs(number))[::-1])
        result = int(reverseNumber)
        print(f"reverse number {reverseNumber}  result {result}")
        print(f"result {result} 2**31 -1 {2**31-1}  -2**31 {-2**31}")
        if result >= 2**31 -1 or result <= -2**31:
            return 0
        elif number < 0:
            return -1 * result
        else:
            return result


s = Solution()
print(s.reverseInteger(-10))
print(s.reverseInteger(123))
print(s.reverseInteger(-324))
