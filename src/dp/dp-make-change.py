# Copyright (C) 2020 Akash Nag
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#	
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#	
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



# Problem description:
# -------------------
# Given a set of M coins and an amount A, find how many coins of each type
# must be given to make change for that amount, ensuring a minimum number of
# coins are used.

# Running-time: O(A.m)

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