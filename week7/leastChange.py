# Using a bottom up approach for dp

# First goal is to create a dp array and init with amount + 1 or float('inf'), doesn't matter
# as long as it is greater than the amount that we're looking for
# NOTE: This is crucial as we're trying to find a value that is less than the current 
# number of "coins" needed, we'll be comparing at the end to find our answer

def foo(amount: int, coins: list) -> int:
    dp = [float('inf')]*(amount + 1)
    
    dp[0] = 0
    
    # We're going to solve subproblems from 0...N
    for i in range(1, amount + 1):
        # We're going to create branches for the coins we have
        for coin in coins:
            # If the current coin is less than the current amount
            # We're going to find the minimum amount of coins needed
            # for that specific amount and set it to dp[amount]
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1) # +1, because we used a coin, so it is an "extra" step
                
            
    return -1 if dp[amount] >= float('inf') else dp[amount]
                  
if __name__ == "__main__":
    amount = 11
    coins = [1, 2, 5]
    print(foo(amount, coins))