class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0] * (amount + 1)
        arr[0] = 1

        for j in coins:
            for i in range(amount + 1):
                if i + j <= amount:
                    arr[i + j] += arr[i]

        return arr[amount]