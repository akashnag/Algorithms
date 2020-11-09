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
# Given a list of N numbers, sort it in non-decreasing order 
# using randomized Quick-Sort.

# Average-case: O(n lg(n))
# Worst-case: O(n^2)

import random

# function to swap two elements of a list
def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

def partition(a, lb, ub):
	pivot = random.choice(range(lb,ub+1))
	down = lb
	up = ub

	while(down < up):
		while(down < ub and a[down] <= a[pivot]):
			down += 1		
		while(up > lb and a[up] > a[pivot]):
			up -= 1
		if(down < up):
			swap(a, down, up)

	swap(a, pivot, up)
	return up

# function to perform quick-sort
def quickSort(a,lb,ub):
	if(lb>=ub):
		return
	else:
		k = partition(a,lb,ub)
		quickSort(a,lb,k-1)
		quickSort(a,k+1,ub)

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke quick sort
	quickSort(a,0,n-1)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(a[i])

main()