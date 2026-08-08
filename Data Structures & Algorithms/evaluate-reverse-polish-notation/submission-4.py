class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == '+':
                second = nums.pop()
                first = nums.pop()
                nums.append(first + second)
            elif token == '-':
                second = nums.pop()
                first = nums.pop()
                nums.append(first - second)
            elif token == '*':
                second = nums.pop()
                first = nums.pop()
                nums.append(first * second)
            elif token == '/':
                second = nums.pop()
                first = nums.pop()
                nums.append(int(first / second))
            else:
                nums.append(int(token))

        print(nums)
        return nums[0]
        
                