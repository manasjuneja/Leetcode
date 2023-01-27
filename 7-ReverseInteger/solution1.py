class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        rev = int(str(x)[::-1])
        if rev > 2**31 - 1:
            return 0
        else :
            return rev * sign
