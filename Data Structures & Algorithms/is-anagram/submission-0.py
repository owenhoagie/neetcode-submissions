class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both, compare - o(nlogn)
        # loop through and count letters - o(n)
        if len(s) != len(t):
            return False

        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        
        for char in t:
            if char in chars:
                chars[char] -= 1
            else:
                return False

        for char in chars:
            if chars[char] != 0:
                return False
        
        return True