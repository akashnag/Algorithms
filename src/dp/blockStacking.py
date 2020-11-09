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
# Given a set of blocks, each with a length, width and height. Find the
# optimal way to stack the blocks to achievet the maximum height, provided
# no block is stacked on top of a smaller block (smaller by length or by width).

# Running-time: O(m.n)

import math

class Block:
	def __init__(self, name, length, width, height):
		self.name = name
		self.length = length
		self.width = width
		self.height = height
	
	def __str__(self):
		return self.name + " [" + str(self.length) + "x" + str(self.width) + "x" + str(self.height) + "]"

def filter(blocks, ind, i):
	indices = []
	n = len(blocks)
	if(i>=n):
		return None
	for j in range(n):
		if(j in ind and j!=i and blocks[j].length <= blocks[i].length and blocks[j].width <= blocks[i].width):
			indices.append(j)
	return indices

n = 5
rb = []
winner = []

def hash(indices):
	bitVector = [ 0 for i in range(n) ]
	for i in indices:
		bitVector[i]=1
	sum=0
	c=0
	for i in range(n-1,-1,-1):
		sum += bitVector[i] * int(math.pow(2,c))
		c += 1
	return sum

def compute(blocks, indices):
	global rb
	global winner
	
	if(len(indices)==0):
		return 0
	i = indices[0]
	fbi = filter(blocks,indices,i)
	m1 = blocks[i].height + compute(blocks, fbi)
	if(len(indices)==1):
		m2 = 0
	else:
		m2 = rb[hash(indices[1:])]
	hi = hash(indices)
	
	if(m1>=m2):
		rb[hi] = m1
		winner[hi] = winner[hash(fbi)]
		if(winner[hi]==None):
			winner[hi] = [ i ]
		else:
			winner[hi].append(i)
	else:
		rb[hi] = m2
		winner[hi] = winner[hash(indices[1:])]

	return rb[hi]

def main():
	global n
	global rb
	global winner

	n = int(input("Enter the # of blocks: "))
	blocks = [ None for i in range(n) ]
	for i in range(n):
		print("Enter data for block #" + str(i+1) + ":")
		name = input("\tName: ")
		length = int(input("\tLength: "))
		width = int(input("\tWidth: "))
		height = int(input("\tHeight: "))
		blocks[i] = Block(name, length, width, height)
	
	#n = 5
	#blocks = [
	#	Block("A", 5, 3, 2),
	#	Block("B", 1, 5, 3),
	#	Block("C", 7, 4, 1),
	#	Block("D", 5, 1, 3),
	#	Block("E", 6, 4, 4)
	#]

	blocks.sort(key = lambda x: (x.length, x.width), reverse=True)
		
	max = int(math.pow(2,n))
	rb = [ 0 for i in range(max) ]
	winner = [ None for i in range(max) ]

	for i in range(n-1, -1, -1):
		compute(blocks,range(i,n))

	print("\nMaximum height achievable: " + str(rb[max-1]))
	print("Optimal stacking order: ")	
	for i in winner[max-1]:
		print(blocks[i])

main()