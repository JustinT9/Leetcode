class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)): 
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)): 
            for j in range(len(matrix)//2): 
                matrix[i][j], matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j], matrix[i][j]