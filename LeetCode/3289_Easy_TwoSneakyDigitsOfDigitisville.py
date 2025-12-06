class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        dupes = []
        for i in range(len(nums)):
            if nums[i] in d:
                dupes.append(nums[i])
                if len(dupes) == 2:
                    return dupes
            else:
                d[nums[i]] = 1
