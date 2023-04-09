class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
                    break
            return True

        a = 0
        l = len(nums)
        for i in range(l):
            if prime(nums[i][i]):
                a = max(a, nums[i][i])

            if prime(nums[i][l-i-1]):
                a = max(a, nums[i][l-i-1])

        return a

