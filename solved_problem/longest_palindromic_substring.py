# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        min_start = 0
        max_len = 1
        for i in range(len(s)):
            if((len(s) - i) < ((max_len + 1)/ 2)):
                break
            j = i
            k = i
            while k < len(s) - 1 and s[k + 1] == s[k]:
                k += 1
            while k < len(s) - 1 and j > 0 and s[k + 1] == s[j - 1]:
                j -= 1
                k += 1
            new_len = k - j + 1
            if new_len >= max_len:
                max_len = new_len
                min_start = j
        return s[min_start:(min_start + max_len)]
