class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(curr, hset):
            if len(curr) == n:
                res.append(curr.copy())
                return

            for i in range(n):
                if i not in hset:
                    hset.add(i)
                    curr.append(nums[i])
                    dfs(curr, hset)
                    hset.remove(i)
                    curr.pop()

        dfs([], set())
        return res