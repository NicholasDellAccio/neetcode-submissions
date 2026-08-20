class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        temp = 1
        for i in range(len(nums)):
            prefix.append(temp)
            temp *= nums[i]

        postfix = [1]*len(nums)
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = temp
            temp *= nums[i]

        for i in range(len(nums)):
            prod = postfix[i] * prefix[i]
            res.append(prod)

        return res