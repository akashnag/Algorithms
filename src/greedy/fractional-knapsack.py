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
# into the knapsack to maximize the total value of the knapsack.

# Running-time: O(n)

# The greedy algorithm takes the objects in decreasing order of the
# ratio between value to size.

class Item:
	def __init__(self, name, size, value):
		self.name = name
		self.size = size
		self.value = value
		self.ratio = value / size

class KnapsackItem:
	def __init__(self, item, fraction):
		self.item = item
		self.fraction = fraction

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
	
	warehouse.sort(key = lambda x: x.ratio, reverse=True)
	knapsack = list()
	remainingCapacity = s
	totalValue = 0

	for i in range(n):
		if(warehouse[i].size <= remainingCapacity):
			knapsack.append(KnapsackItem(warehouse[i], 1.0))
			remainingCapacity = remainingCapacity - warehouse[i].size
			totalValue = totalValue + warehouse[i].value
		else:
			fraction = remainingCapacity / warehouse[i].size
			knapsack.append(KnapsackItem(warehouse[i], fraction))
			remainingCapacity = 0
			totalValue = totalValue + (fraction * warehouse[i].value)
			break
	
	print("Knapsack Contents:\n\n#\tFRAC.\tNAME\tSIZE\tVALUE")
	i = 1
	for obj in knapsack:
		f = obj.fraction
		fs = round(obj.item.size * f, 2)
		fv = round(obj.item.value * f, 2)
		print(str(i) + "\t" + str(round(f,2)) + "\t" + str(obj.item.name) + "\t" + str(fs) + "\t" + str(fv))
		i = i + 1

	print("\nTotal value of the knapsack: " + str(round(totalValue,2)))

main()