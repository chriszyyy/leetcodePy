class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dic = {}
        for i in range(len(nums)):
            if nums[i] in buff_dic:
                return [buff_dic[nums[i]], i]
            else:
                buff_dic[target - nums[i]] = i
        
