class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        a = 0
        while len(nums)>0:
            if len(nums) == 1:
                l = nums.pop()
                
                
            else:
                x = nums.pop(0)
                y = nums.pop()
                
                m = list(str(x))
                n = list(str(y))
                k = m + n
                
                l = int("".join(k))
            a += l
            
            
        return a
