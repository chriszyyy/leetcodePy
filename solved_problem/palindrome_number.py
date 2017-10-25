import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = math.floor(x / 10)
        return  x == rev or x == math.floor(rev / 10)

#python3 need use math.floor
#python2 juste x / b --> floor
