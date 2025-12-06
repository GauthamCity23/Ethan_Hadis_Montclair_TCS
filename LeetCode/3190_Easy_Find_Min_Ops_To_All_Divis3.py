class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        not_divis_by_thr = 0
        for i in nums:
            if i % 3 != 0:
                not_divis_by_thr += 1
        return not_divis_by_thr
