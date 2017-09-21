class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        first_str = strs[0]
        for i in range(len(first_str)):
            k = 1
            while k < len(strs):
                if i > (len(strs[k]) - 1) or strs[k][i] != first_str[i]:
                    return first_str[:i]
                k += 1
        return first_str
