# problem with solution was that it was too slow because of the recursive calls that did 
# scale too well as n approached towards the larger numbers 

# time took: 1hr 20m 
class Solution(object):
    def __init__(self):
        self.ret = 0

    def climbStairs(self, n):
        if n == 0:
            self.ret += 1
        else:
            if n-1 >= 0:
                self.climbStairs(n-1)
            if n-2 >= 0:
                self.climbStairs(n-2)
        return self.ret

# memoized solution 
class Solution(object):
    def climbStairs(self, n):
        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        elif n == 2: 
            return 2
        else: 
            f = [i for i in range(n)]
            f[0], f[1] = 1, 2 
            for i in range(2, n):
                f[i] = f[i-1] + f[i-2]
        return f[n-1] 



            
        
        
