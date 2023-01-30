def generate(numRows):
    # initializes the arrays intially with zero 
    pascal = [[1]*(i+1) for i in range(numRows)]
    # goes through the cells of pascal 2 by 2 array 
    for i in range(numRows):
        for j in range(1,i):
            # reassigns the numbers from the previous row from the second number to the second to last number 
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

# top down recursive 
# time complexity is O(n^2) since we visiting each array and within each array we are traversing through it  
# space complexity is O(n^2) since we are allocating an array and within each array we are allocating a subarray of size n 
class Solution:
    def generate(self, n: int) -> List[List[int]]:        
        def helper(n):
            if n:
                helper(n-1)                 # generate above row first
                ans.append([1]*n)           # insert current row into triangle
                for i in range(1, n-1):     # update current row values using above row
                    ans[n-1][i] = ans[n-2][i] + ans[n-2][i-1]
        ans = []
        helper(n)
        return ans