class Solution(object):
    def intersect(self, nums1, nums2):
        ret, nums = [], {}
        if len(nums1) < len(nums2): 
            for num in nums2: 
                try:
                    nums[num] += 1 
                except KeyError: 
                    nums[num] = 1 

            for num in nums1: 
                try: 
                    if nums[num] != 0: 
                        ret.append(num)
                        nums[num] -= 1
                except KeyError:  
                    continue 
        else: 
            for num in nums1: 
                try:
                    nums[num] += 1 
                except KeyError: 
                    nums[num] = 1

            for num in nums2: 
                try: 
                    if nums[num] != 0:
                        ret.append(num)
                        nums[num] -= 1 
                except KeyError: 
                    continue 
        
        return ret 