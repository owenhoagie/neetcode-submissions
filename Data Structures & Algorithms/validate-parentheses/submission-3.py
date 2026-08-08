class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in chars.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                if stack.pop() != chars[char]:
                    return False
        
        return len(stack) == 0
