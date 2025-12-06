class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         numbers_times = {}
         for i in range(len(nums)):
            key = nums[i]
            if key not in numbers_times:
                numbers_times[key] = 1
                if numbers_times[key] > len(nums) / 2:
                    return key
            else:
                numbers_times[key] += 1
                if numbers_times[key] > len(nums) / 2:
                    return key
