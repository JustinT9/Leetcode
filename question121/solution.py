class Solution:
    def maxProfit(self,prices):
        # initalization 
        left = 0 # Buy
        right = 1 # Sell

        # tracker variable 
        max_profit = 0
        # traverse through the entire list 
        while right < len(prices):
            currentProfit = prices[right] - prices[left] # our current Profit
            # to calculate the max everytime 
            if prices[left] < prices[right]:
                # determine the most profit
                max_profit = max(currentProfit,max_profit)
            else:
                # otherwise adjust the smallest value 
                left = right
            # keep on pushing the right tracker forward 
            right += 1 
        return max_profit

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        # always have the min price 
        min_price = min(min_price, price)
        # calculate the profit for a potential max profit 
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# more concise way 
def maxProfit(self, prices: List[int]) -> int:
	if not prices:
		return 0

	maxProfit = 0
	minPurchase = prices[0]
	for i in range(1, len(prices)):		
		maxProfit = max(maxProfit, prices[i] - minPurchase)
		minPurchase = min(minPurchase, prices[i])
	return maxProfit