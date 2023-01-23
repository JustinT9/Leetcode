def generate(numRows):
    # initializes the arrays intially with zero 
    pascal = [[1]*(i+1) for i in range(numRows)]
    # goes through the cells of pascal 2 by 2 array 
    for i in range(numRows):
        for j in range(1,i):
            # reassigns the numbers from the previous row from the second number to the second to last number 
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal