class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = list(ransomNote)
        m = list(magazine)

        x = True

        for i in rn :
            if i in m:
                m.remove(i)

            else :
                x = False
                break

        return x


