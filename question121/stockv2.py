# keeps reupdating the pointers through the sliding window technique 
# this is the dynamic version since the window resizes 
# time complexity: O(n) since it goes through the list 
# space complexity: O(1) since it does not have any dynamically allocated container in the heap 
class Solution(object):
    def maxProfit(self, prices):
        l = 0 
        r = 1 
        profit = 0 

        while (r < len(prices)):
            if prices[l] > prices[r]:
                l = r
            else: 
                profit = max(prices[r]-prices[l], profit)
            r += 1 
        return profit 