class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in d:
                return [d[looking_for], i]
            else:
                d[nums[i]] = i
