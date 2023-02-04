class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 6:
            return False
            
        while (n>6):
            sum = 0
            x = str(n)

            for i in x:
                sum = sum + int(i)**2

            if sum == 1:
                return True
            elif sum < 6:
                return False
            else:
                n = sum

