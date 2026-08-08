class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        zeroCount = 0
        maxProduct = 1
        for index, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
                if zeroCount == 2:
                    return res

                temp = maxProduct
                if index == len(nums)-1:
                    res[index] = temp
                    return res
                
                for j in range(index+1, len(nums)):
                    temp *= nums[j]

                res[index] = temp
            else:
                maxProduct *= num
        
        if zeroCount > 0:
            return res
        
        for index, num in enumerate(nums):
            res[index] = maxProduct // num

        return res