class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        def binary(n):
            global x
            x = []
            if n >= 1:
                binary(n//2)
            x.append(n%2)


        binary(n)
        x.pop(0)
        print(x)

        e = 0
        o = 0

        for i in range(len(x)):
            if i%2 == 1 and x[i]==1:
                o += 1
            elif i%2 == 0 and x[i]==1:
                e += 1

        return[e,o]
