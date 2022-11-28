class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        x = []

        # name variables properly
        n = min(strs, key=len)



        for i in n:
            x.append(i)




        for word in strs:
            m = 0
            for letter in x:

                if letter != word[m]:
                    x = x[:m]
                m += 1


        return "".join(x)

