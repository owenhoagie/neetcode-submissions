class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ")":
                if len(stack) == 0:
                    return False

                res = stack.pop()
                if res != "(":
                    return False
            elif char == "}":
                if len(stack) == 0:
                    return False
                    
                res = stack.pop()
                if res != "{":
                    return False
            elif char == "]":
                if len(stack) == 0:
                    return False
                    
                res = stack.pop()
                if res != "[":
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
