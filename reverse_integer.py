class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        r = int(`s * x`[::-1])
        return s * r * (r < 2**31)

#python2 has cmp for comparing two number
#python3 is (a > b) - (a < b)
