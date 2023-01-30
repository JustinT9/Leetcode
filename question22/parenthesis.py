# generated one more permutation for some reason and it also printed them in the wrong order 
# took around 40m 
class Solution(object):
    def generateParenthesis(self, n):
        count = 0
        parenthesis = []
        string = ""
        self.generate(count, n, string, parenthesis)
        return parenthesis

    def generate(self, count, n, string, parenthesis): 
        if count == n:
            if string not in parenthesis:
                parenthesis.append(string)
            return 
        self.generate(count+1, n, "("+string+")", parenthesis)
        self.generate(count+1, n, "()"+string, parenthesis)
        self.generate(count+1, n, string+"()", parenthesis)

