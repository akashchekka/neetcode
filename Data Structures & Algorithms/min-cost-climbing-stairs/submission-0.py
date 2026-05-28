class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            cost_1 = dp[i - 1] + cost[i - 1]
            cost_2 = dp[i - 2] + cost[i - 2]

            dp[i] = min(cost_1, cost_2)
        
        return dp[n]


        
            