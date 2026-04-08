class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = nums[0]

        for i in nums:
            currsum = max(currsum, 0)
            currsum += i
            maxsum = max(maxsum, currsum)
        
        return maxsum