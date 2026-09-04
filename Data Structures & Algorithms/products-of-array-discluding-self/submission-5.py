class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        answer = [0] * len(nums)
        product = 1
        for num in nums:
            if num == 0:
                zeroCount += 1
                if zeroCount >= 2:
                    return answer
            else:
                product *= num

        for index, num in enumerate(nums):
            if num == 0:
                answer[index] = product
            else:
                if zeroCount > 0:
                    answer[index] = 0
                else:
                    answer[index] = product // num
        
        return answer