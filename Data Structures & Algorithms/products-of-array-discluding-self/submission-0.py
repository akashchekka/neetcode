class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        n = len(nums)

        for i in range(1, n):
            res.append(nums[i - 1] * res[i - 1])

        postfix = nums[n - 1]
        count = n - 2

        while count >= 0:
            res[count] *= postfix
            postfix *= nums[count]
            count -= 1

        return res