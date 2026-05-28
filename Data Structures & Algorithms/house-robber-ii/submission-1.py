class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def max_sum(nums):
            n = len(nums)
            prev = nums[0]
            prev2 = 0

            for i in range(1, n):
                take = nums[i]
                if i > 1: take += prev2

                nontake = prev
                cur = max(take, nontake)

                prev2 = prev
                prev = cur

            return prev

        return max(max_sum(nums[:len(nums) - 1]), max_sum(nums[1:]))