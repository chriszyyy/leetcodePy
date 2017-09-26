class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums) <= 3:
            return sum(nums)

        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - res) > abs(target - s):
                    res = s
                    if res == target:
                        return res
                if target < s:
                    k -= 1
                else:
                    j += 1
        return res
