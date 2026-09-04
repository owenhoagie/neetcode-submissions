class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        left = [1] * (l+1)
        right = [1] * (l+1)

        answer = [1] * l
        
        for index in range(l):
            right_index = (l - 1) - index
            left[index+1] *= nums[index] * left[index]
            right[right_index] *= nums[right_index] * right[right_index+1]

        for index in range(l):
            answer[index] = left[index] * right[index+1]

        return answer
