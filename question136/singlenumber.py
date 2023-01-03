# took around 30m 
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        count = 0
        retNum = 0 
        number = nums[0]

        for i in range(len(nums)): 
            count += 1

            if number != nums[i] or i == len(nums)-1: 
                if count == 1: 
                    retNum = number 
                count = 0 
                number = nums[i]
        return retNum

        