# done in 15m
class Solution(object):
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower(): 
                    return False
                i += 1; j -= 1 
            elif not(s[i].isalnum()) and s[j].isalnum(): 
                i += 1 
            elif s[i].isalnum() and not(s[j].isalnum()):
                j -= 1 
            else: 
                i += 1; j -= 1 

        return True 