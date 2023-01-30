class Solution(object):
    def letterCombinations(self, digits):
        letters = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}

        stringCombo = ""
        combinations = []
        if (len(digits) == 0): 
            return combinations

        self.findCombinations(digits, letters, combinations, stringCombo, 0)
        return combinations 

    def findCombinations(self, digits, letters, combinations, stringCombo, letterIndex):
        if letterIndex == len(digits):
            combinations.append(stringCombo)
            return 
        for letter in letters[digits[letterIndex]]: 
            stringCombo += letter
            self.findCombinations(digits, letters, combinations, stringCombo, letterIndex+1)
            stringCombo = stringCombo[:len(stringCombo)-1]