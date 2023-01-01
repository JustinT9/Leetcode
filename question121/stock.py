# issue was that it was not able to pass the remainding test cases 
# 46m 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i1 = 0
        i2 = 0
        lowest = 0 
        highest = 0

        lowest = min(prices)
        highest = max(prices)
        i1 = prices.index(lowest)
        i2 = prices.index(highest)
        
        if i1 < i2: 
            return highest-lowest 
        elif i1 > i2 and i1 != len(prices)-1:
            highest = max(prices[:i1])
            i2 = prices.index(highest)
            lowest = min(prices[:i2])
            if highest > lowest:
                return highest-lowest
        elif i1 > i2 and i1 == len(prices)-1:
            lowest = min(prices[:i1])
            if i2 == 0: 
                return 0 
            if highest > lowest: 
                return highest-lowest
        return 0

# another solution but it took way too long other test cases 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        largest = 0
        result = 0
        for i in range(len(prices)):
            largest = max(prices[i:])
            if largest - prices[i] > result: 
                result = largest - prices[i]

        if result <= 0: 
            return 0 
        return result 