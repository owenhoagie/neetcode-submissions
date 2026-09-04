class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set(nums)
        starters = []

        for num in nums:
            if num-1 not in seen:
                starters.append(num)

        longest = 0
        for num in starters:
            current = 1
            increment = num+1
            while increment in seen:
                increment += 1
                current += 1
            
            longest = max(current, longest)

        return longest

