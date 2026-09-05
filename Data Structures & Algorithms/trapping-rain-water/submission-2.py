class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)

        left = 0
        right = len(height) - 1
        bound = [[] for i in range(l)]

        left_max = 0
        right_max = 0

        prefix = [0] * l
        suffix = [0] * l

        while left < l and right >= 0:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
 
            if left < right:
                bound[left] = [left_max, height[left], 0]
                bound[right] = [0, height[right], right_max]
            elif left == right:
                bound[left] = [left_max, height[left], right_max]
            else:
                bound[right][2] = right_max
                bound[left][0] = left_max

            left += 1
            right -= 1

        # print(bound)
        ans = 0
        for i in range(l):
            ans += min(bound[i][0], bound[i][2]) - bound[i][1]

        return ans