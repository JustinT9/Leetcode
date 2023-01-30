# done in 20m~
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        rows = []
        for i in range(numRows):
            row = [] 
            row.append(1)
            if i >= 2: 
                for j in range(len(rows[i-1])-1):
                    row.append(rows[i-1][j] + rows[i-1][j+1])
            if i >= 1:
                row.append(1)
            rows.append(row)
        return rows 

# memoized version 
# time complexity is O(n^2) since we going through each row and within each row we are going through its numbers 
# space complexity is O(n^2) since we are allocating a 2d array of n arrays with n numbers 
class Solution(object):
    def generate(self, numRows):
        ret = [[1 for j in range(i)] for i in range(1, numRows+1)]
        for i in range(2, len(ret)): 
            for j in range(len(ret[i])-2): 
                ret[i][j+1] = ret[i-1][j] + ret[i-1][j+1]
        return ret 

