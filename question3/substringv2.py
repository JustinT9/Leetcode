class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0 
        ret = 0
        letters = {} 

        for r in range(len(s)): 
            if s[r] in letters:
                while s[r] in letters:
                    del letters[s[l]]
                    l += 1 
            letters[s[r]] = r 
            ret = max(ret, len(letters))
        return ret 
