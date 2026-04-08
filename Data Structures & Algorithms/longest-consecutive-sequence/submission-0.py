class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0

        for i in nums:
            if i - 1 not in s:
                temp = i
                count = 0
                while temp in s:
                    count += 1
                    temp += 1
                res = max(res, count)      

        return res