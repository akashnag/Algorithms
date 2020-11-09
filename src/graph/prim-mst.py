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
# Find the Minimal Spanning Tree of a graph using Prim's algorithm

def extract_min(Q, key):
	min_node = -1
	for i in Q:
		if(key[i] < 0): continue
		if(min_node < 0 or key[i] < key[min_node]): min_node = i
	
	Q.remove(min_node)
	return min_node

def prim(n, weights):
	Q = [ i for i in range(n) ]
	key = [ -1 for i in range(n) ]
	parent = [ -1 for i in range(n) ]
	key[0] = 0
	S = []

	while(len(Q) > 0):
		u = extract_min(Q, key)
		S.append(u)
		for v in range(n):
			if(u!=v and weights[u][v] > -1 and v in Q and (key[v] == -1 or weights[u][v] < key[v])):
				key[v] = weights[u][v]
				parent[v] = u

	return parent

def main():
	n = int(input("Enter the number of vertices: "))
	w = [ [ 0 for _ in range(n) ] for _ in range(n) ]
	
	for i in range(n):
		w[i][i] = 0
		for j in range(i+1,n):
			w[i][j] = int(input(f"[V{i+1}->V{j+1}] Enter edge cost (>0) or -1 for no edge: "))
			w[j][i] = w[i][j]

	parents = prim(n,w)
	print("Root=V1")
	for v in range(1,n):
		p = parents[v]
		c = w[v][p]
		print(f"V{v+1}<--({c})-->V{p+1}")

main()