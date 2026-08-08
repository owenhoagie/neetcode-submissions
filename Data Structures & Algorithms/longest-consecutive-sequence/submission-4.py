class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                streak, curr = 1, num+1
                while curr in nums:
                    streak += 1
                    curr += 1
                highest = max(highest, streak)

        return highest