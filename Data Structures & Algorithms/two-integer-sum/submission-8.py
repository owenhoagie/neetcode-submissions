class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            if (diff:= target-num) in seen:
                return [seen[diff], index]
            seen[num] = index

        return []