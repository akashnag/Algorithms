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
# Given a list of N numbers, sort it in non-decreasing order using Selection Sort.

# Running-time: O(n^2)

# function to swap two elements of a list
def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

# function to find the minimum element in a list
def findMinPosition(a, low, high):
	minPos = low
	for i in range(low+1, high+1):
		if(a[i] < a[minPos]): minPos = i
	return minPos

# function to perform selection-sort
def selectionSort(a, n):
	for i in range(n-1):
		j = findMinPosition(a,i,n-1)
		swap(a,i,j)

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke selection sort
	selectionSort(a,n)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(a[i])

main()