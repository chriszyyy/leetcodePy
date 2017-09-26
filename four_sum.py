# Given an array S of n integers, are there elements a, b, c,
# and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

class Solution(object):
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        print nums[l], nums[r]
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
                        # print results

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


# class Solution(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         sum_to = 0
#         res_tup = []
#         if len(nums) < 4:
#             return res_tup
#         if sum(nums) == target and len(nums) == 4:
#             return [nums]
#
#         for i in range(len(nums) - 3):
#             if i == 0 or nums[i] != nums[i - 1]:
#                 for j in range(i + 1, len(nums) - 2):
#                     if j == i + 1 or nums[j] != nums[j - 1]:
#                         lo = j + 1
#                         hi = len(nums) - 1
#                         sum_to = target - nums[i] - nums[j]
#                         while lo < hi:
#                             if nums[lo] + nums[hi] == sum_to:
#                                 res_tup.append([nums[i], nums[j], nums[lo], nums[hi]])
#                                 while lo < hi and nums[lo] == nums[lo + 1]:
#                                     lo += 1
#                                 while lo < hi and nums[hi] == nums[hi - 1]:
#                                     hi -= 1
#                                 lo += 1
#                                 hi -= 1
#                             elif nums[lo] + nums[hi] < sum_to:
#                                 lo += 1
#                             else:
#                                 hi -= 1
#         return res_tup
