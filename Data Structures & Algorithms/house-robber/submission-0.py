class Solution:
    def rob(self, nums: List[int]) -> int:
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