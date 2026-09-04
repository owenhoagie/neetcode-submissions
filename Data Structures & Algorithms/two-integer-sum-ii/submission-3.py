class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)

        leftIndex = 0
        rightIndex = l - 1

        while leftIndex < rightIndex:
            total = numbers[leftIndex] + numbers[rightIndex]
            if total < target:
                leftIndex += 1
            elif total > target:
                rightIndex -= 1
            else:
                return [leftIndex + 1, rightIndex + 1]
        
        return [-1, -1]