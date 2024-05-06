def max_profit(prices):
    min_price = float('inf')
    max_price = 0

    for price in prices:
        min_price = min(min_price, price)
        max_price = max(max_price, (price - min_price))
    
    return max_price


prices = [7,6,4,3,1]
print(max_profit(prices))
