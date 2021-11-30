import re
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        newPattern = "^{}$".format(pattern)
        find = re.match(newPattern, text)
        return True if find else False

S = Solution()
print(S.isMatch("aab", "c*aa*b"))


