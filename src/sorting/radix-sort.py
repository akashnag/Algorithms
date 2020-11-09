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

def radixSort(arr,n,m):
	exp = 1
	while(m//exp > 0):
		countSort(arr,n,exp)
		exp *= 10

def countSort(arr,n,exp):
	out = [ 0 for i in range(n) ]
	count = [ 0 for i in range(10) ]

	for i in range(n):
		count[(arr[i] // exp) % 10] += 1
	
	for i in range(1,10):
		count[i] += count[i-1]
	
	for i in range(n-1, -1, -1):
		out[count[(arr[i] // exp) % 10] - 1] = arr[i]
		count[(arr[i] // exp) % 10] -= 1
	
	for i in range(n):
		arr[i] = out[i]

def main():
	# input the list of numbers
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))

	# invoke radix sort
	m = max(a)
	radixSort(a,n,m)

	# display the sorted list
	print("Sorted list:")
	for i in range(n):
		print(a[i])

main()