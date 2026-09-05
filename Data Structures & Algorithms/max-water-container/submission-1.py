class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        left = 0
        right = l - 1
        area = 0

        # area = (right-left) * min(heights[left], heights[right])

        while left < right:
            ca = (right-left) * min(heights[left], heights[right])
            area = max(area, ca)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                caR = (right-1-left) * min(heights[left], heights[right-1])
                caL = (right-left+1) * min(heights[left+1], heights[right])

                # area = max(area, caR, caL)
                left += 1
                right -= 1

        return area

