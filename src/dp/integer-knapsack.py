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
# Given a set of N objects, each with a size and a value; and given a
# knapsack with total capacity S; find a subset of objects to pack
# into the knapsack to maximize the total value of the knapsack. Each
# object must be included totally or not at all.

# Running-time: O(S.N)

# The DP algorithm uses the formula: KS(S,i) = MAX{ KS(S,i+1), v(i)+KS(S-s(i),i+1) }
# where s(i) and v(i) are the size and value of the i-th object respectively
# and i loops for all objects in some order.

class Item:
	def __init__(self, name, size, value):
		self.name = name
		self.size = size
		self.value = value

	def __str__(self):
		return str(self.name) + "\t" + str(self.size) + "\t" + str(self.value)

class KnapsackItem:
	def __init__(self, value, index, included, item):
		self.item = item
		self.index = index
		self.value = value
		self.included = included

def main():
	s = int(input("Enter the total capacity of the knapsack: "))
	
	n = int(input("Enter the total number of items: "))
	warehouse = [None for i in range(n)]
	
	for i in range(n):
		print("Item #" + str(i+1) + ":")
		name = input("\tName: ")
		size = int(input("\tSize: "))
		value = int(input("\tValue: "))
		warehouse[i] = Item(name, size, value)
	
	#n = 3
	#s = 6
	#warehouse = [
	#	Item("A", 1, 50),
	#	Item("B", 4, 140),
	#	Item("C", 2, 60)
	#]

	knapsack = [None for i in range(n)]
	for i in range(n):
		knapsack[i] = [None for i in range(s+1)]
	
	for i in range(n-1, -1, -1):
		for x in range(s+1):
			maxPos = -1
			maxVal = 0
			maxIncluded = False
			for k in range(i,n):
				itemSize = warehouse[k].size
				included = False
				if(itemSize > x):
					if(k==n-1):
						v = 0
					else:
						v = knapsack[k+1][x].value
				else:
					included = True
					if(k==n-1):
						val = 0
					else:
						val = knapsack[k+1][x-itemSize].value
					v = warehouse[k].value + val
				
				if(v > maxVal):
					maxVal = v
					maxPos = k
					maxIncluded = included
			
			if(maxPos == -1):
				item = None
			else:
				item = warehouse[maxPos]
			knapsack[i][x] = KnapsackItem(maxVal, maxPos, maxIncluded, item)
	
	print("\nKnapsack Contents:\n\n#\tNAME\tSIZE\tVALUE")
	remainingCapacity = s
	j = 0
	while(not knapsack[j][s].included):
		j = j + 1
	current = knapsack[j][s]
	i = 1
	totalValue = 0
	while(current.item != None):
		item = current.item
		print(str(i) + "\t" + str(item))
		totalValue = totalValue + item.value
		remainingCapacity = remainingCapacity - item.size
		
		j = current.index
		while(j>=0 and j<n and (not knapsack[j][remainingCapacity].included)):
			j = j + 1
		if(j<0 or j>=n): break
		
		current = knapsack[j][remainingCapacity]
		i = i + 1

	print("\nTotal value of the knapsack: " + str(totalValue))

main()