class Solution:
    def numberOfSteps(self, num: int) -> int:
        x = 0
        while num != 0:
            if num % 2 == 1:
                num = num -1
                x += 1

            else:
                num = num/2
                x += 1

        return x
