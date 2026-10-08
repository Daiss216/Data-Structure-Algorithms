class Solution(object):
    def maxProfit(self, prices):
        #2-Pointers
        l= 0   #Buy
        r= 1  #Sell
        maxProf= 0

        while r < len(prices):
            if prices[l] < prices[r]:    #profit check
                profit= prices[r] - prices[l]
                maxProf= max(maxProf, profit)

            else:
                l = r
            r += 1

        return maxProf