class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Convert all negatives to 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # nums[abs(nums[i]) - 1] *= -1  
        for i in range(n):
            value = abs(nums[i])
            if 1 <= value <= n:
                if nums[value - 1] > 0:
                    nums[value - 1] *= -1
                elif nums[value - 1] == 0:
                    nums[value - 1] = -1 * (n + 1)

        for i in range(1, n+1):
            if nums[i - 1] >= 0:
                return i

        return n + 1