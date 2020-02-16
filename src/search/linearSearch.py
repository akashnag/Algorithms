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
# Consider a list of N numbers given in any arbitrary order. Given another
# number S, find whether or not it exists in the given list.

# Running-time: O(n)

# a function to search a list for a number and return its index if found,
# otherwise return -1
def linearSearch(a, n, s):
	for i in range(n):
		if(a[i] == s):
			return i
	return -1

def main():
	# input the list and the number to search for
	n = int(input("Enter the size of the list: "))
	a = [0 for i in range(n)]
	for i in range(n):
		a[i] = int(input(str(i+1) + ". Enter a number: "))
	s = int(input("Enter a number to search for: "))

	# perform linear search
	p = linearSearch(a,n,s)
	if(p == -1):
		print("The number you searched for does not exist in the list")
	else:
		print("The number was found at index #" + str(p))

main()