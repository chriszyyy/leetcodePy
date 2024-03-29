class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        l = 0
        r = len(height) - 1
        while(l < r):
            maxarea = max(maxarea, min(height[l] * (r - l), height[r] * (r - l)))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxarea
