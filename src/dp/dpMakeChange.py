# Copyright 2020 Akash Nag

# Licensed under the MIT License; you may not use this file except 
# in compliance with the License. You may obtain a copy of the 
# License at:
#
#    https://opensource.org/licenses/MIT
#
# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without restriction, 
# including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



# Problem description:
# -------------------
# Given a set of M coins and an amount A, find how many coins of each type
# must be given to make change for that amount, ensuring a minimum number of
# coins are used.

# Use Dynamic Programming (DP) to find the solution using the formula:
# MC(C,A) = MIN{1 + MC(C, A-c[I])} over all 0 <= I < M
# where C = { c[0], c[1], ... , c[M-1] } is the set of M coins
# and A is the amount to be changed

def main():
	# initialize infinity to a large number
	infinity = 999999999

	# input the types of coins available, and the amount to change
	m = int(input("How many types of coins are there? "))
	coins = [0 for i in range(m)]
	for i in range(m):
		coins[i] = int(input("Enter coin value: "))
	amount = int(input("Enter amount to change: "))

	# initialize the array to store the min. number of coins 
	# required, to infinity; except for amount=0, which ofcourse uses no coins
	usedCoins = [0 for i in range(amount+1)]
	numCoins = [infinity for i in range(amount+1)]
	numCoins[0] = 0
	
	for i in range(1,amount+1):					# for each possible amount
		min = infinity
		minCoin = -1
		for j in range(m):						# for each type of coin
			if(i >= coins[j]):					# consider only coins which are less than the amount
				c = numCoins[i - coins[j]]		# number of coins required still if we include this coin
				if(c < min):
					min = c						# find the minimum
					minCoin = j
		numCoins[i] = 1 + min					# add +1 to the min to account for the coin we just included
		usedCoins[i] = minCoin					# store backtracking information to find the actual coins used
	
	if(numCoins[amount] >= infinity):
		print("Not possible")
	else:
		print("Total # of coins required = " + str(numCoins[amount]))
		print("Coins used: ")
		# Backtrack to find the actual coins used
		a = amount
		i = usedCoins[a]
		while(a > 0):
			print(coins[i])
			a = a - coins[i]
			i = usedCoins[a]

main()