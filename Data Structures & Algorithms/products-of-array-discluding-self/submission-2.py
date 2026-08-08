class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * l
        for ind in range(1, l):
            pre[ind] = pre[ind-1] * nums[ind-1]

        post = [1] * l
        for ind in range(l-2, -1, -1):
            post[ind] = post[ind+1] * nums[ind+1]

        print(pre)
        print(post)
        ans = [0] * l
        for ind in range(l):
            ans[ind] = pre[ind] * post[ind]

        return ans