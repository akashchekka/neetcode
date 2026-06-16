class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            if total == 0:
                res.append(curr.copy())
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]: continue
                if candidates[j] > total: break

                curr.append(candidates[j])
                dfs(j + 1, curr, total - candidates[j])
                curr.pop()

        dfs(0, [], target)
        return res