class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount, product = 0, 1
        res = [0] * len(nums)
        for num in nums:
            if num:
                product *= num
            else:
                zeroCount += 1
        
        if zeroCount > 1:
            return res
        
        for index, num in enumerate(nums):
            if zeroCount == 1:
                res[index] = product if num == 0 else 0
            else:
                res[index] = product // num
        
        return res