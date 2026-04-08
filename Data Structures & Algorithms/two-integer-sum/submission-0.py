class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = dict()

        for i in range(len(nums)):
            if target - nums[i] in hset:
                return [hset[target - nums[i]], i]
            else:
                hset[nums[i]] = i
