class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_int = 0
        if 'IV' in s:
            res_int -= 2
        if 'IX' in s:
            res_int -= 2
        if 'XL' in s:
            res_int -= 20
        if 'XC' in s:
            res_int -= 20
        if 'CD' in s:
            res_int -= 200
        if 'CM' in s:
            res_int -= 200

        for i in range(len(s)):
            if s[i] == 'I':
                res_int += 1
            elif s[i] == 'V':
                res_int += 5
            elif s[i] == 'X':
                res_int += 10
            elif s[i] == 'L':
                res_int += 50
            elif s[i] == 'C':
                res_int += 100
            elif s[i] == 'D':
                res_int += 500
            elif s[i] == 'M':
                res_int += 1000
        return res_int    
