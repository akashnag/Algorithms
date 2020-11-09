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
# Consider a grid of size M x N, with the bottom-left point being (1,1)
# and top-right being (M,N). Calculate the number of distinct paths there
# are to reach position (M,N) from the starting position (1,1) when the only
# moves allowed at each position are UP and RIGHT.

# Running-time: O(m.n)

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