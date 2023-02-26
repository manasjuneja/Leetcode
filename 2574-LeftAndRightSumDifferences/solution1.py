class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ls = 0
        leftsum = []
        rs = 0
        rightsum = []
        answer = []

        for i in nums:
            leftsum.append(ls)
            ls += i

        for j in nums[::-1]:
            rightsum.append(rs)
            rs += j

        rightsum = rightsum [::-1]

        for k in range(len(nums)):
            a = leftsum[k] - rightsum[k]
            if a < 0:
                a = a * (-1)
            answer.append(a)


        return answer
