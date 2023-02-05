class Solution(object):
    def searchRange(self, nums, target):
        low, high = 0, len(nums)-1   
        while low <= high: 
            mid = (low + high) / 2
            if nums[mid] < target: 
                low = mid+1
            elif nums[mid] > target: 
                high = mid-1
            elif nums[low] == target and nums[high] != target and nums[mid] > target:
                high = mid-1 
            elif nums[low] == target and nums[high] != target and nums[mid] == target: 
                return [low, mid] 
            elif nums[low] != target and nums[high] == target and nums[mid] < target:
                low = mid+1 
            elif nums[low] != target and nums[high] == target and nums[mid] == target: 
                return [mid, high]
            elif nums[low] != target and nums[high] != target and nums[mid] == target: 
                high = (mid + high) / 2
                low = (low + mid) / 2 
            elif nums[mid] == target and low == high:  
                return [mid, mid]  
            elif nums[low] == target and nums[high] == target: 
                return [low, high] 
        return [-1, -1]