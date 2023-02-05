class Solution(object):
    def combinationSum(self, candidates, target):
        ret, temp = [], []
        return self.combinations(temp, ret, candidates, target) 

    def combinations(self, temp, ret, candidates, target): 
        if target < 0:
            temp.pop()
            return 
        elif target == 0: 
            ret.append(temp)
            temp.pop()
            return ret
        for num in candidates: 
            temp.append(num)
            self.combinations(temp, ret, candidates, target-num)
            
        return ret  
        
            