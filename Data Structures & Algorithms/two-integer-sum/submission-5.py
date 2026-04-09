class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for index, num in enumerate(nums):
            if target-num in prev.keys():
                return [prev[target-num], index]
            
            prev[num] = index

        return []
