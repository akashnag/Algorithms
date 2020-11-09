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
# Sort a list of N numbers in ascending order using Heap Sort

# Running-time: O(n.lg(n))

import math

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

def max_heapify(a, i, n):
	left = 2*i + 1
	right = 2*i + 2
	if(left < n and right < n):
		if(a[left] > a[i] and a[left] >= a[right]):
			swap(a, i, left)
			max_heapify(a, left, n)
		elif(right < n and a[right] > a[i] and a[right] >= a[left]):
			swap(a, i, right)
			max_heapify(a, right, n)
	elif(left < n and right >= n and a[left] > a[i]):
		swap(a, i, left)
		max_heapify(a, left, n)

def build_max_heap(a, n):
	i = math.ceil((n-1)/2)
	while(i >= 0):
		max_heapify(a,i,n)
		i -= 1

def heap_sort(a, n):
	build_max_heap(a,n)
	sorted_list = [ 0 for i in range(n) ]
	while(n > 0):
		swap(a, 0, n-1)
		sorted_list[n-1] = a[n-1]
		n -= 1
		max_heapify(a,0,n)
	return sorted_list

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke merge sort
	sorted_list = heap_sort(a,n)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(sorted_list[i])

main()