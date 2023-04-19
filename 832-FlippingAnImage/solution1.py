class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        x =[]
        for i in image:
            x.append(i[::-1])
        for m in range(len(x)):
            for n in range(len(x[m])):
                if x[m][n] == 0:
                    x[m][n] = 1
                else:
                    x[m][n] = 0

        return x
