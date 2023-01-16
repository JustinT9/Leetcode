# algorithm: sliding window -- involves two pointers a left and right where the right is constantly updated and the left is updated conditionally -- 
# in this case when there are duplicates identified 
# time complexity: O(n) since we are going through the entire string of size n 
# space complexity: O(m) where m represents the number of unique letters  


def longestSubstring1(s): 
    # contains the letters to keep track of there being duplicates or not 
    charSet = set()
    # left pointer that contains index  
    l = 0 
    ret = 0

    # constantly update the right pointer 
    for r in range(len(s)): 
        # to remove the duplicates including the words before it 
        while s[r] in charSet: 
            charSet.remove(s[l])
            l += 1 
        # constantly append the letters 
        charSet.add(s[r])
        # max is the difference between the indexes + 1 since indexes start at 0 
        ret = max(ret, r - l + 1)
    return ret 

# O(m) space complexity where m represents the number of unique words 
def lengthOfLongestSubstring(s):
    # initialize variables and dictionary to store/track duplicates 
    start = maxLength = 0
    usedChar = {}
    
    # iterate the right pointer 
    for i in range(len(s)):
        # if there is a duplicate and that the left pointer is on the duplicate word 
        # or before it update it so the left pointer removes the duplicate word by
        # being ahead of it 
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        # otherwise recalculate the max value 
        else:
            maxLength = max(maxLength, i - start + 1)

        # update the index of the letter so duplicates can be removed 
        usedChar[s[i]] = i

    return maxLength

def lengthOfLongestSubstring(s):
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            """
            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            """
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output