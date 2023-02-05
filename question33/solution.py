class Solution: 
    def search(self, nums, target): 
        l, r = 0, len(nums) - 1

        while l <= r: 
            # floor division 
            mid = (l + r) // 2 
            if target == nums[mid]:
                return mid 

            # determine if left is sorted portion of array 
            if nums[l] <= nums[mid]:
                # if it is  
                if target > nums[mid] or target < nums[l]: 
                    l = mid + 1 
                else: 
                    r = mid - 1
            # otherwise right is sorted portion of the array 
            else:  
                if target < nums[mid] or target > nums[r]: 
                    r = mid - 1 
                else: 
                    l = mid + 1 

        return -1 

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid
            
            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]: # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1

class Solution:
    def search(self, A: List[int], target: int) -> int:
        n = len(A)
        left, right = 0, n - 1
        if n == 0: return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target: return mid
            
            # inflection point to the right. Left is strictly increasing
            if A[mid] >= A[left]:
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # inflection point to the left of me. Right is strictly increasing
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1