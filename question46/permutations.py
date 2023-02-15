# took 25 m 
class Solution(object):
    def permute(self, nums):
        ret = []

        def permutations(temp, ret, nums):
            if len(temp) == len(nums): 
                ret.append(temp[:])
                return 
            for i in range(len(nums)): 
                if nums[i] not in temp:
                    temp.append(nums[i])
                    permutations(temp, ret, nums)
                    temp.pop() 
            
        permutations([], ret, nums)
        return ret 
