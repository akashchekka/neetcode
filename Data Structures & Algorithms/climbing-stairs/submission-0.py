class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1, 2]
        arr = [0] * (n + 1)
        arr[0] = 1

        for i in range(len(arr)):
            for j in nums:
                if i + j <= n:
                    arr[i + j] += arr[i]
        
        return arr[n]