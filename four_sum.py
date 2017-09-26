# Given an array S of n integers, are there elements a, b, c,
# and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        sum_to = 0
        res_tup = []
        if len(nums) < 4:
            return res_tup
        if sum(nums) == target and len(nums) == 4:
            return [nums]

        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        lo = j + 1
                        hi = len(nums) - 1
                        sum_to = target - nums[i] - nums[j]
                        while lo < hi:
                            if nums[lo] + nums[hi] == sum_to:
                                res_tup.append([nums[i], nums[j], nums[lo], nums[hi]])
                                while lo < hi and nums[lo] == nums[lo + 1]:
                                    lo += 1
                                while lo < hi and nums[hi] == nums[hi - 1]:
                                    hi -= 1
                                lo += 1
                                hi -= 1
                            elif nums[lo] + nums[hi] < sum_to:
                                lo += 1
                            else:
                                hi -= 1
        return res_tup
