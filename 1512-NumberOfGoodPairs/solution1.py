class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = 0
        while len(nums)>0:
            a = nums.pop(0)
            for i in nums:
                if i == a:
                    n += 1

        return n
