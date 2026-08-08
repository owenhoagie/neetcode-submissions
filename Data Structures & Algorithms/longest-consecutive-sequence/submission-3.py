class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                t = num+1
                streak = 1
                while t in nums:
                    streak += 1
                    t += 1
                highest = max(highest, streak)

        return highest