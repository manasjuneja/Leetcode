class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        mx = []
        num = list(number)
        for i in range(len(num)):
            if num[i] == digit:

                if i == 0:
                    a = "".join(num[i+1:])

                elif i == len(num)-1:
                    a = "".join(num[:i])

                else:
                    a = "".join(num[:i] + num[i+1:])

                mx.append(int(a))

        return str(max(mx))


