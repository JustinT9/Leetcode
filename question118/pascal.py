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


