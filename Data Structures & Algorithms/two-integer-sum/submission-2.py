class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for index, num in enumerate(nums):
            optimal = target-num
            if optimal in nummap.keys():
                return [nummap[optimal], index]
            
            nummap[num] = index
            