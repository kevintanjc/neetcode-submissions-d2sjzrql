from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)

        @cache
        def dp(i, shares):
            if i > days - 1:
                return 0

            # currently holding onto 1 share, looking to sell
            if shares == 1:

                # choice 1: sell now
                best = prices[i] + dp(i + 1, 0)

                #choice 2: sell later
                best = max(best, dp(i + 1, 1))

                return best
            
            # currently have not bought any share
            if shares == 0:

                # choise 1: buy now
                best = -1 * prices[i] + dp(i + 1, 1)

                #choice 2: buy later
                best = max(best, dp(i + 1, 0))

                return best

        return dp(0, 0)
                

