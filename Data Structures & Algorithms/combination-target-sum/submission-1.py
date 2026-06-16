class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, curr, total):
            if total == 0:
                res.append(curr.copy())
                return

            for j in range(i, n):
                if nums[j] > total: continue

                curr.append(nums[j])
                dfs(j, curr, total - nums[j])
                curr.pop()

        dfs(0, [], target)
        return res
