class Solution: 
    def generateParenthesis(self, n):
        # add open if open < n
        # add close if close < open 
        # valid parenthesis open == n == close
        
        stack = []
        res = []

        def backtrack(openN, closedN): 
            if openN == closedN == n: 
                res.append("".join(stack))
                return 
            
            if openN < n: 
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN: 
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() 
            
        backtrack(0, 0)
        return res 

# my solution
class Solution(object):
    def generateParenthesis(self, n):
        ret = []

        def generate(temp, ret, opened, closed, n):
            if opened == n and closed == n: 
                ret.append(temp)
                return 
            
            if closed < opened: 
                generate(temp+")", ret, opened, closed+1, n)
            if opened < n: 
                generate(temp+"(", ret, opened+1, closed, n)
            
        generate("", ret, 0, 0, n)
        return ret 