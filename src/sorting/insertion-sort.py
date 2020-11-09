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
# Given a list of N numbers, sort it in non-decreasing order using Insertion-Sort.

# Running-time: O(n^2)

# function to perform insertion-sort
def insertionSort(a, n):
	for i in range(1,n):
		copy = a[i]
		j = i-1
		while(j > -1 and a[j] > copy):
			a[j+1] = a[j]
			j = j - 1
		a[j+1] = copy

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke insertion sort
	insertionSort(a,n)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(a[i])

main()