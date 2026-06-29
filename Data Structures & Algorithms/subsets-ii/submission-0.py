class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def backtrack(i, curr):
            res.append(curr.copy())
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]: continue
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return res
    