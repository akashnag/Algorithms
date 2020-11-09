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
# Consider a set of M tasks T = { t(1), t(2), ... t(M) }. 
# Each task t(i) = ( s(i), f(i), w(i) ) consists of:
# a starting time s(i), a finishing time f(i), and weight w(i). 
# Assuming a single resource on which to execute tasks,
# determine a subset S of tasks that can be scheduled so that:
# 	- no two pair of tasks overlap in time
#	- the sum of the weights of all tasks scheduled is maximized

# Dynamic Programming Solution:
# Using the recurrence: MAXW(T) = MAX{w(i) + MAXW(S^i)} for all i
# where: T is the set of tasks
# and S^i = { t(j) | s(j) >= f(i) } is a subset of T
# The tasks are considered in non-increasing order of f(i).
# Running-time: O(n^2)

class Task:
	# constructor to initialize task
	def __init__(self, id, s, f, w):
		self.id = id
		self.start = s
		self.finish = f
		self.weight = w
	
	# check if a given task begins after this task ends
	def endsBefore(self, t):
		return(True if (t.start >= self.finish) else False)

def main():
	# input tasks
	n = int(input("Enter the # of tasks: "))
	tasks = [None for i in range(n)]
	for i in range(n):
		print("Task #" + str(i+1) + ":")
		s = int(input("\tEnter starting-time: "))
		f = int(input("\tEnter finishing-time: "))
		w = int(input("\tEnter weight: "))
		if(s >= f or w < 1):
			print("Invalid input!")
			return
		tasks[i] = Task(i+1, s, f, w)
	
	# sort the tasks in non-increasing order of finishing-time
	tasks.sort(key = lambda x: x.finish, reverse=True)
	
	# initialize
	costs = [0 for i in range(n)]
	winners = [None for i in range(n)]
	lastWinnerID = -1

	# perform the scheduling
	for i in range(n):
		maxWeight = 0
		maxTask = None

		for j in range(n):
			if(tasks[j].start >= tasks[i].finish):
				c = costs[j]
				if(c > maxWeight):
					maxWeight = c
					maxTask = j
		
		costs[i] = maxWeight + tasks[i].weight		# apply the recurrence
		winners[i] = maxTask						# store backtracking info
	
		if(lastWinnerID < 0 or costs[i] > costs[lastWinnerID]):
			lastWinnerID = i						# keep track of the task from which to start backtracking

	# print the scheduled set of tasks
	print("\nScheduled tasks:")
	print("#\tSTART\tFINISH")
	i = lastWinnerID
	totalWeight = 0
	count = 0
	while(i != None):
		t = tasks[i]
		print(str(t.id) + "\t" + str(t.start) + "\t" + str(t.finish))
		count += 1
		totalWeight += t.weight
		i = winners[i]

	print("Total tasks scheduled: " + str(count) + " with total weight = " + str(totalWeight))

main()