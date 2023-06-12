class Solution:
    def countVowelStrings(self, n: int) -> int:

        x = 0

        a = [[1, 1, 1, 1, 1]]

        while x < (n-1):

            b = [sum(a[len(a)-1]), sum(a[len(a)-1])-a[len(a)-1][0], sum(a[len(a)-1])-a[len(a)-1][0]-a[len(a)-1][1], sum(a[len(a)-1])-a[len(a)-1][0]-a[len(a)-1][1]-a[len(a)-1][2], 1]

            a.append(b)

            x += 1

        return sum(a[len(a)-1])

