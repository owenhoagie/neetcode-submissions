class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both, compare - o(nlogn)
        # loop through and count letters - o(n)
        return sorted(s) == sorted(t)