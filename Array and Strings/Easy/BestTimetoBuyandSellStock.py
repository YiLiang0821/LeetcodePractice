#121
import operator
def maxProfit(prices):
    minForBuy = float('inf')
    mixForProfit = 0
    for p in prices:
        if p < minForBuy:
            minForBuy = p
        elif p - minForBuy > mixForProfit:
            mixForProfit = p - minForBuy
            
    return mixForProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))