class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r_sum = []
        s = 0
        for i in nums:
            s += i
            r_sum.append(s)
        return r_sum
