class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

        
# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         zz = []
#         for i in range(numRows):
#             zz.append([])
#         k = 0 #colunm
#         j = 0 #row
#         zigzag = True
#         index_c = 0
#         while index_c < len(s):
#             k = k % numRows
#             if j % 2 != 0:
#                 if zigzag:
#                     zz[k].append(' ')
#                     zigzag = False
#                     index_c -= 1
#                 else:
#                     zz[k].append(s[index_c])
#                     zigzag = True
#             else:
#                 zz[k].append(s[index_c])
#             index_c += 1
#             k += 1
#             if k == numRows:
#                 j += 1
#                 zigzag = True
#         print_zz = ''
#         return_zz =''
#         for k in range(numRows):
#             for j in range(len(zz[k])):
#                 print_zz += zz[k][j]
#                 if zz[k][j] != ' ':
#                     return_zz += zz[k][j]
#             print_zz += '\n'
#         print(print_zz)
#         return return_zz
