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
# Search for a pattern in a text using the Boyer-Moore algorithm.

# Running-time: O(n.m) worst-case, O(n+m) best-case

def boyer_moore(text, pattern):
	n = len(text)
	m = len(pattern)
	i = m-1
	j = m-1

	while(i<=n-1):
		if(pattern[j] == text[i]):
			if(j==0):
				return i
			else:
				i -= 1
				j -= 1
		else:
			try:
				i += m - min([ j, 1+pattern.rindex(text[i])])
			except:
				i += m - min([ j, 0 ])
			j = m-1

	return -1

def main():
	text = input("Enter the text to search in: ")
	pattern = input("Enter a pattern to search for: ")
	index = boyer_moore(text, pattern)
	if(index < 0):
		print("Pattern not found")
	else:
		print("Pattern found at index: " + str(index))

main()