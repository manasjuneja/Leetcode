class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x = s.split()
        y = []
        for i in range(k):
            y.append(x[i])
        return " ".join(y)
