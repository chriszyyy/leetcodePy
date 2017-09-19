class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            s = 1
        elif x < 0:
            s = -1
        else:
            s = 0
        r = int(`s * x`[::-1])
        return s * r * (r < 2**31)
