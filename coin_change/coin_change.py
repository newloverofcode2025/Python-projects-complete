def coinChange(coins: list[int], amount: int) -> int:
    """
    Find the minimum number of coins required to make up a given value.
    """
    # Initialize the dp array with a value representing infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

    # Fill the dp array
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
        ([1], 1),
        ([1], 2)
    ]
    for coins, amount in test_cases:
        print(f"Minimum coins needed to make {amount} with coins {coins}: {coinChange(coins, amount)}")