class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)

        left = [1] * l
        right = [1] * l
        
        left[0] = nums[0]
        right[-1] = nums[-1]

        for index in range(1, l):
            left[index] *= nums[index] * left[index-1]

        for index in range(l-2, -1, -1):
            right[index] *= nums[index] * right[index+1]

        answer = [1 * right[1]]
        right.append(1)

        for index in range(l-1):
            answer.append(left[index] * right[index+2])

        return answer