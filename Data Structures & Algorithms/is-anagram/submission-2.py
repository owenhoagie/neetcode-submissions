class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = dict()

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter:
                return False

            counter[char] = counter[char] - 1
            if counter[char] == 0:
                counter.pop(char)

        return len(counter) == 0
        
