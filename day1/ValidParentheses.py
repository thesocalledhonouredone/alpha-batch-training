class Solution:
    def isValid(self, s: str) -> bool:
        myst = list()

        for i in s:
            if i == '{' or i == '(' or i == '[':
                myst.append(i)
            elif len(myst) == 0:
                return False
            elif i == ')' and myst[-1] == '(':
                myst.pop()
            elif i == ']' and myst[-1] == '[':
                myst.pop()
            elif i == '}' and myst[-1] == '{':
                myst.pop()
            else:
                return False
            
        if len(myst) == 0:
            return True
        else:
            return False