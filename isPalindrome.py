class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if x < 0:
            return False
        for i in range(len(y)):
            start = y[i]
            end = y[-(i+1)]
            if start == end:
                s = True
            else:
                return False
        return s
