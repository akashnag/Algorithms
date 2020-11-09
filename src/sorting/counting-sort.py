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
# Sort a list of N numbers in ascending order using Counting-Sort

# Running-time: O(n+m)

def countSort(a, n, m):
	c = [ 0 for i in range(m+1) ]
	for i in range(n):
		c[a[i]] += 1
	
	k=-1
	for i in range(m+1):
		for j in range(c[i]):
			k += 1
			a[k] = i

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke counting sort
	m = max(a)
	countSort(a,n,m)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(a[i])

main()