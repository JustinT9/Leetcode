# binary search     
# took about 25m however memory usage can optimized 
class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1 
        return self.search(low, high, nums, target)


    def search(self, low, high, nums, target): 
        if low == high: 
            if (target < nums[low]) or (target == nums[low]):
                return low
            elif target > nums[low]: 
                return low+1


        else: 
            middle = (low+high)/2 
            if target < nums[middle]:
                return self.search(low, middle, nums, target)
            elif target > nums[middle]: 
                return self.search(middle+1, high, nums, target)
            else: 
                return middle 