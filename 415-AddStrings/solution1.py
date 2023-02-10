class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        d = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}

        n1 = 0
        for i in num1:
            n1 = n1*10 + d[i]

        n2 = 0
        for j in num2:
            n2 = n2*10 + d[j]

        return str(n1 + n2)


