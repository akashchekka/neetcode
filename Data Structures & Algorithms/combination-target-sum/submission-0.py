class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= n:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
