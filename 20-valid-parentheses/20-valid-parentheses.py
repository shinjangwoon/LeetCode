class Solution:
    def isValid(self, s: str) -> bool:
        dic_s = {')':'(', 
                 '}':'{',
                 ']':'['}
        stack = []
        for i in s:
            if i not in dic_s:
                stack.append(i)
            elif not stack or dic_s[i] != stack.pop():
                return False
        return not stack

            