class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            bit = n&1
            res += bit
            n >>= 1

        return res
