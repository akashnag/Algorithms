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
# Consider a grid of size M x N, with the bottom-left point being (1,1)
# and top-right being (M,N). Calculate the number of distinct paths there
# are to reach position (M,N) from the starting position (1,1) when the only
# moves allowed at each position are UP and RIGHT.

# The solution uses Dynamic Programming (DP) to keep track of the solutions
# of each point we calculate in ascending order of rows and columns. This
# ensures previous values are always available to calculate the next value.
# The DP solution is implemented as follows:
# Let A = no. of distinct paths to point (i,j)
# Let B = no. of distinct paths to reach its left neighbour (i,j-1)
# Let C = no. of distinct paths to reach its bottom neighbour (i-1,j)
# Then, A = B + C, because there is only 1 way of reaching (i,j) from its left or bottom neighbour

def main():
	# input grid size
	m = int(input("Enter M: "))
	n = int(input("Enter N: "))

	# define a grid of size M x N, and
	# initialize left and bottom bborder costs to 1
	x = [0 for i in range(m)]
	for i in range(m):
		x[i] = [0 for j in range(n)]
		for j in range(n):
			x[0][j] = 1
		x[i][0] = 1
	
	# invoke the DP algorithm to determine cost of reaching the destination
	cost = findCostDP(x, m, n)
	print("Total cost: " + str(cost))

def findCostDP(x, m, n):
	for i in range(1,m):							# for each row
		for j in range(1,n):						# for each column
			x[i][j] = x[i-1][j] + x[i][j-1]			# compute the DP equation
	return x[m-1][n-1]								# return the value at the destination point

main()