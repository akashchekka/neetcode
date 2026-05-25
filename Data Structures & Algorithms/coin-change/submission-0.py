class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [None] * (amount + 1)
        arr[0] = 0

        for i in range(amount + 1):
            for j in coins:
                if arr[i] is not None and i + j <= amount and (arr[i + j] is None or arr[i] + 1 < arr[i + j]):
                    arr[i + j] = arr[i] + 1

        return arr[amount] if arr[amount] is not None else -1