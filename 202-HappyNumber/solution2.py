class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        for i in nums:
            a.append(i*i)
        for i in range(len(a)-1,0,-1):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]

        return a
