class Solution:
    def countBits(self, n: int) -> List[int]:
        x = []
        for i in range(n+1):
            b = format(i, 'b')
            a = 0
            for j in b:
                if j == '1':
                    a += 1
            x.append(a)

        return x
