class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sum_to = 0
        res_tup = []
        if len(nums) < 3:
            return res_tup
        if sum(nums) == 0 and len(nums) == 3:
            return [nums]

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                lo = i + 1
                hi = len(nums) - 1
                sum_to = 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == sum_to:
                        res_tup.append([nums[i], nums[lo], nums[hi]])
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
