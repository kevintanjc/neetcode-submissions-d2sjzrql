class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_buy = prices[0]
        biggest_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > lowest_buy:
                biggest_profit = max(biggest_profit, prices[i] - lowest_buy)
            elif prices[i] < lowest_buy:
                lowest_buy = prices[i]

        return biggest_profit


