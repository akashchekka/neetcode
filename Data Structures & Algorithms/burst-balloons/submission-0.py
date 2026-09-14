class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        a = [1] + nums + [1]
        memo = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n, 0, -1):
            for j in range(1, n+1):
                if i > j: continue
                res = float('-inf')
                for k in range(i, j + 1):                   # j runs from 1 to n
                    cost = a[i - 1] * a[k] * a[j + 1]
                    cost += memo[i][k - 1] + memo[k + 1][j] # j = n => k = n in one iteration, and memo[k + 1] = memo[n + 1]. So memo should be of size n + 2 to access (n + 1)th element.
                    res = max(res, cost)
                memo[i][j] = res

        return memo[1][len(nums)]