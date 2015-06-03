target_sum = 200
coins = [1 ,2, 5, 10, 20, 50, 100, 200]

# Ways for all sums up to target
ways = [1] + [0]*target_sum

# Test all coins as start value
for coin in coins:
	# Calulate all possible sums for this coin
    for i in range(coin, target_sum+1):
    	# Add a all possible ways for the ways of this sum - coin.
    	# Example: 3 ways to make a hundred. If target is 200 and 
    	# using a 100 bill, the amount of ways to make 200 is the
    	# 3 ways to make the first hundred.
        ways[i] += ways[i-coin]

print ways[target_sum]