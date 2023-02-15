class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = 0
        for i in range(len(number)):
            if number[i] == digit:
                last = i
                if i + 1 < len(number) and number[i + 1] > digit:
                    break
