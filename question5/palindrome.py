# hard to understand what to implement 
# tried to do it recursively but it did not end up working 
# apparently some dynamic programming is involved 
class Solution(object):
    def longestPalindrome(self, s):
        length = 0 
        palindrome = ""
        for i in range(len(s)): 
            temp = self.construct(s, s[i], i-1, i+1)
            if len(temp) > length: 
                palindrome = temp
                length = len(temp)
        return palindrome

    def construct(self, s, letter, start, end): 
        if start <= 0 and end >= len(s) - 1: 
            return letter 
        elif start == 0 and end <= len(s) - 1: 
            if s[end] != letter: 
                return letter
            else: 
                return self.construct(s, letter + s[end], start, end+1)
        elif start >= 0 and end == len(s) - 1: 
            if s[start] != letter: 
                return letter  
            else:
                return self.construct(s, s[start] + letter, start-1, end)
        elif start >= 0 and end <= len(s) - 1: 
            if s[start] != s[end]: 
                return letter 
            return self.construct(s, s[start] + letter + s[end], start-1, end+1)


        