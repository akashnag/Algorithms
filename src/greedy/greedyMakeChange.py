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

# This program uses a Greedy solution to solve the problem, which of course
# does not always work. e.g. Consider C={1,3,5,6,7} be the set of 5 coins,
# and the amount to be changed is 11. This algorithm returns 3 coins, while
# the correct answer should be 2.
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