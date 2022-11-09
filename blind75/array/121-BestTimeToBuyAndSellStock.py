def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # if the prices array has less than 2 prices, return no profit
    n = len(prices)
    if n < 2:
        return 0
    
    # start with an outrageous value that will be overwritten by the smallest value
    minVal = 10000 
    # begin with 0 max profit 
    maxProfit = 0

    # iterate through the array
    for i in range(len(prices)):

        # compare minimum of current element to the known smallest element
        minVal = min(prices[i], minVal)
        # find maximum between the profit of current element minus the smallest element, 
        # and the known max profit
        maxProfit = max(prices[i] - minVal, maxProfit)
    
    return maxProfit

if __name__ == "__main__":
    p = [7, 1, 5, 3, 6, 4]
    print("maxProfit(", "Prices:", p, ") -->", maxProfit(p))