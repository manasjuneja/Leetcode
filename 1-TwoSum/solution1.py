class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        while len(nums) > 0:
            a = nums.pop(0)
            for i in range(len(nums)):
                if a + nums[i] == target:
                    return x, i+x+1
            x +=1
