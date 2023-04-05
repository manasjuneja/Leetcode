class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        x = []

        for i in nums1:
            if i in nums2:
                x.append(i)

        if len(x) != 0:
            return min(x)

        a = min(nums1)
        b = min(nums2)

        x = a*10 + b
        y = b*10 + a

        return min(x,y)
