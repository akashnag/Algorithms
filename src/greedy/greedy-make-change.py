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
# must be given to make change for that amount, using as few coins as possible.

# Running-time: O(m)

# The greedy algorithm considers, at each step, the largest coin that can 
# be used, and then uses it, subtracts the value from the amount, and 
# then continues.

def main():
	# input the types of coins and the amount to make change for
	m = int(input("How many types of coins are there? "))
	coins = [0 for i in range(m)]
	coinCount = [0 for i in range(m)]
	for i in range(m):
		coins[i] = int(input("Enter coin value: "))
	amount = int(input("Enter amount to change: "))

	# sort the coins in descending order of value, initialize count to 0
	coins.sort(reverse=True)
	count = 0
	for i in range(m):
		# consider those coins which have lower value than the remaining amount
		if(amount >= coins[i]):
			x = (amount // coins[i])	# compute the # of coins required
			count += x					# add it to the total count
			coinCount[i] = x			# record it against that coin
			amount %= coins[i]			# compute the amount remaining to be changed
			if(amount==0): 				# if done, break
				break
	
	if(amount > 0):
		print("Not possible")			# if still amount remains, then no solution possible
	else:
		print("Total # of coins required = " + str(count) + " as follows:")
		for i in range(m):
			if(coinCount[i] > 0):		# consider only those coins which are actually used
				print(str(coinCount[i]) + " coin(s) of value " + str(coins[i]) + " = " + str(coins[i] * coinCount[i]))

main()