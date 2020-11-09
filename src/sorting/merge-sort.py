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
# Sort a list of N numbers in ascending order using Merge Sort

# Running-time: O(n.lg(n))

def mergeSort(x, low, high):
	if(low >= high):
		return
	else:
		mid = (low + high)//2
		mergeSort(x, low, mid)
		mergeSort(x, mid+1, high)
		merge(x, low, mid, high)

def merge(x, low, mid, high):
	i = low
	j = mid+1
	c = [0 for k in range(high-low+1)]
	k = 0

	# copy using two-finger algorithm
	while(i <= mid and j <= high):
		if(x[i] < x[j]):
			c[k] = x[i]
			i += 1
		else:
			c[k] = x[j]
			j += 1
		k += 1
	
	# copy remaining
	while(i <= mid):
		c[k] = x[i]
		i += 1
		k += 1

	# copy remaining
	while(j <= high):
		c[k] = x[j]
		j += 1
		k += 1

	# copy back into original list
	i = low
	for k in range(high-low+1):
		x[i] = c[k]
		i += 1

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke merge sort
	mergeSort(a,0,n-1)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(a[i])

main()