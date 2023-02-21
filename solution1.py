class Solution:
    def isValid(self, s: str) -> bool:
            left = []
            for i in s:
                if i in ['(', '{', '[']:
                    left.append(i)
                elif i == ')' and len(left) != 0 and  left[-1] == '(':
                    left.pop()
                elif i == '}' and len(left) != 0 and left[-1] == '{':
                    left.pop()
                elif i == ']' and len(left) != 0 and left[-1] == "[":
                    left.pop()
                else:
                    return False
            if len(left) == 0:
                return True
            else:
                return False
