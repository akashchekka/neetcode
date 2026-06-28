class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        res = []
        res.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                idx = bisect_left(res, nums[i])
                res[idx] = nums[i]
        
        return len(res)
