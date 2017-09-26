class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]

        for i in str(digits):
            tempres = []
            for char in mapping[int(i)]:
                for j in res:
                    tempres.append(j + char)
            res = tempres
        return res
