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
# Implement Breadth-First-Search on a graph

def bfs(n, adj, node_values, source, search_value):
	visited = []
	frontier = []
	frontier.append(source)

	while(len(frontier) > 0):
		top = frontier.pop(0)
		visited.append(top)
		if(node_values[top] == search_value):
			return True
		else:
			for i in range(top+1,n):
				if(adj[top][i] == 1 and i not in visited):
					frontier.append(i)
	return False

def main():
	n = int(input("Enter the number of vertices: "))
	adj = [ [ 0 for _ in range(n) ] for _ in range(n) ]

	node_values = [ 0 for i in range(n) ]
	for i in range(n):
		node_values[i] = int(input(f"[V{i+1}] Enter the value of the node: "))

	for i in range(n):
		adj[i][i] = 1
		for j in range(i+1,n):
			adj[i][j] = int(input(f"[V{i+1}->V{j+1}] Enter 1 for edge, 0 for no edge: "))

	source = int(input(f"Enter the source vertex (1-{n}): "))-1
	sv = int(input("Enter a value to search for: "))

	found = bfs(n, adj, node_values, source, sv)
	if(found):
		print("Value found")
	else:
		print("Value not found")

main()