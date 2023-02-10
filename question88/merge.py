# took 40m but was unsuccessful because of my logical reasonings 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0 and n == 1: 
            nums1[0] = nums2[0]
        else:  
            mPtr, nPtr, iPtr = 0, 0, m-1 
            while mPtr != (m + n):
                if nPtr < n: 
                    if nums1[mPtr] > nums2[nPtr]:
                        temp = nums1[mPtr]
                        nums1[mPtr] = nums2[nPtr]
                        nums1[iPtr] = temp 
                        nPtr += 1; iPtr += 1 
                else: 
                    iPtr -= n
                    while mPtr != (m + n): 
                        if mPtr == (m + n - 2) and (nums1[mPtr] > nums1[mPtr + 1]): 
                            temp = nums1[mPtr] 
                            nums1[mPtr] = nums1[mPtr + 1]
                            nums1[mPtr + 1] = temp  
                            break 
                        elif iPtr < (m + n) and mPtr < (m + n):   
                            if nums1[mPtr] > nums1[iPtr]: 
                                temp = nums1[mPtr]
                                nums1[mPtr] = nums1[iPtr]
                                nums1[iPtr] = temp 
                                iPtr += 1
                        mPtr += 1
                mPtr += 1


            