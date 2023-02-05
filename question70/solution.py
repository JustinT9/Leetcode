def solution1(n):
    # base cases
    if n <= 0: 
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # hardcoding the steps for the first step 
    one_step_before = 2
    two_steps_before = 1
    # varable to keep track of the total number of steps 
    all_ways = 0
    
    # iteration does x amount of times for that specific number 
    # with a build up from the previous iterations 

    # fibonacci sequence question 
    for i in range(2, n):
        # fn = fn-1 + fn-2 
        all_ways = one_step_before + two_steps_before
        # updates the backsteps to calculate the new number 
        # fn-2 = fn-1
        two_steps_before = one_step_before
        # fn-1 = fn 
        one_step_before = all_ways
    
    return all_ways

# more elegant and concise way of doing it 
def solution2(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo ={}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo: # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]
            else:   # Store the recurssion function in the look-up table and reuturn the stored look-up table function
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)


if __name__ == "__main__":
    print(solution2(100))
