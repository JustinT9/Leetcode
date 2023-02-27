class Solution(object):
    def isPowerOfThree(self, n):
        x, product = 0, 1 

        while product <= n:
            if product == n: 
                return True
            product = 3**x  
            x += 1

        return False 
