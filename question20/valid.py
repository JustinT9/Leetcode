# incorrect solution certain test cases were not able to be executed 
# 76 / 92 correct 
# time 1h 20m 
class Solution:
    def isValid(self, s: str) -> bool:
        # create a data structure to store data 
        validCheck = dict()
        for i in range(len(s)):
            if s[i] not in validCheck:
                validCheck[s[i]] = []
            validCheck[s[i]].append(i)
        
        # checks
        if len(validCheck) % 2 != 0:
            return False 
        # check if the brackets have a corresponding bracket
        # of the same type 
        else: 
            # then checks the position of the brackets to see 
            # if they are valid 
            for key in validCheck.keys(): 
                if key == "(":
                    if ")" not in validCheck: 
                        return False
                    if len(validCheck[key]) != len(validCheck[")"]):
                        return False 

                    for i in range(len(validCheck[key])):
                        if (validCheck[key][i] - validCheck[")"][i]) % 2 == 0:
                            return False

                elif key == "{":
                    if "}" not in validCheck: 
                        return False
                    if len(validCheck[key]) != len(validCheck["}"]):
                        return False 

                    for i in range(len(validCheck[key])):
                        if (validCheck[key][i] - validCheck["}"][i]) % 2 == 0:
                            return False

                elif key == "[":
                    if "]" not in validCheck: 
                        return False
                    if len(validCheck[key]) != len(validCheck["]"]):
                        return False

                    for i in range(len(validCheck[key])):
                        if (validCheck[key][i] - validCheck["]"][i]) % 2 == 0:
                            return False 
        return True 