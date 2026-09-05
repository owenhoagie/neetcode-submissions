class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l <= 2:
            return []

        answer = []
        added = set()
        nums.sort()

        for index in range(l-2):
            left_index = index + 1
            right_index = l-1
            base = nums[index]

            while left_index < right_index:
                total = base + nums[left_index] + nums[right_index]
                if total < 0:
                    left_index += 1
                elif total > 0:
                    right_index -= 1
                else:
                    ans = (nums[index], nums[left_index], nums[right_index])
                    if ans not in added:
                        added.add(ans)
                        answer.append([nums[index], nums[left_index], nums[right_index]])
                    left_index += 1
                    right_index -= 1



        return answer