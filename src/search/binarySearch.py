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
# Consider a sorted list of N numbers. Given another number S, determine
# whether or not it exists in the given list.

# Running-time: O(n.lg(n))

def binarySearch(a, low, high, s):
	if(low > high):
		return False
	else:
		mid = (low + high) // 2
		if(s == a[mid]):
			return True
		elif(s < a[mid]):
			return binarySearch(a, low, mid-1, s)
		else:
			return binarySearch(a, mid+1, high, s)

def main():
	# input the list and the number to search for
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))
	s = int(input("Enter a number to search for: "))

	# sort the list in non-decreasing order
	a.sort()

	# perform binary search
	found = binarySearch(a,0,n-1,s)
	if(found):
		print("The number exists in the list")
	else:
		print("The number does not exist in the list")

main()