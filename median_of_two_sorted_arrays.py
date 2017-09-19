class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        empty_list = False
        if len(nums1) == 0:
            return self.returnMedianNumber(nums2)

        if len(nums2) == 0:
            return self.returnMedianNumber(nums1)

        nums3 = []
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            r1 = nums1[i1]
            r2 = nums2[i2]
            if r1 <= r2:
                nums3.append(r1)
                i1 += 1
            else:
                nums3.append(r2)
                i2 += 1
        while i1 < len(nums1):
            r1 = nums1[i1]
            nums3.append(r1)
            i1 += 1
        while i2 < len(nums2):
            r2 = nums2[i2]
            nums3.append(r2)
            i2 += 1

        print(nums3)
        return self.returnMedianNumber(nums3)

    def returnMedianNumber(self, nums):
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2
        else:
            return nums[len(nums)//2]
