class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        x = 0

        while True:
            try:
                nums.remove(0)

            except ValueError:
                break

            else:
                x += 1


        for i in range(x):
            nums.append(0)


