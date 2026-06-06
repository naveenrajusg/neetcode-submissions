class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        ClosetoOpen = {")":"(","]":"[","}":"{"}

        for a in s:
            if a in ClosetoOpen:
                if stack and stack[-1]==ClosetoOpen[a]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(a) 
        
        return True if not stack else False