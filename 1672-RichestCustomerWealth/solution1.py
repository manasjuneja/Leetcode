class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x = 0
        for i in accounts:
            a = 0
            for j in i:
                a += j

            if a > x:
                x = a

        return x
