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
# Given the orders of a set of N matrices, find the cheapest order in
# which to multiply them.

# Running-time: O(n^3)

# The DP algorithm implements the formula: 
# DP(i,j) = MIN( DP(i,k) + DP(k,j) + CoM(A[i:k], A[k:j])) over all k in (i,j)
# where CoM = Cost of Multiplying

class TableEntry:
	def __init__(self, cost, midpoint):
		self.cost = cost
		self.midpoint = midpoint

def main():
	n = int(input("How many matrices do you wish to multiply? "))
	r = [0 for i in range(n+1)]
	r[0] = int(input("Enter the # of rows in matrix #1: "))
	for i in range(1,n+1):
		r[i] = int(input("Enter the # of cols in matrix #" + str(i) + ": "))
	
	#n = 4
	#r = [ 10, 20, 50, 1, 100 ]

	dp = [None for i in range(n+1)]
	for i in range(n+1):
		dp[i] = [None for j in range(n+1)]
	
	infinity = 99999999
	for i in range(1,n+1):
		dp[i][i]=TableEntry(0,-1)
	
	for d in range(1,n):
		for i in range(1,n-d+1):
			j = i + d
			minCost = infinity
			minPos = -1
			for k in range(i,j):
				cost = dp[i][k].cost + dp[k+1][j].cost + (r[i-1] * r[k] * r[j])
				if(cost < minCost):
					minCost = cost
					minPos = k
			dp[i][j] = TableEntry(minCost, minPos)

	print("\nOptimal cost: " + str(dp[1][n].cost))
	printResult(dp,n,1,n)

def printResult(dp, n, row, col):
	if(dp[row][col].midpoint == -1):
		print(" M" + str(row) + " ", end='')
	else:
		k = dp[row][col].midpoint
		print(" (", end='')
		printResult(dp, n, row, k)
		print("x", end='')
		printResult(dp, n, k+1, col)
		print(") ", end='')

main()