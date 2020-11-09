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
# Each task t(i) = ( s(i), f(i)) consists of a starting time s(i) and a
# finishing time f(i). Assuming a single resource on which to execute tasks,
# determine a subset S of tasks that can be scheduled so that:
# 	- no two pair of tasks overlap in time
#	- the total number of tasks scheduled is maximized

# Greedy solution: Use the heuristic Earliest Finish Time (EFT) to
# order the tasks in non-decreasing order of f(i), and for each 
# task selected, remove all incompatible tasks from consideration.
# Running-time: O(n^2)

class Task:
	# constructor to initialize task
	def __init__(self, id, s, f):
		self.id = id
		self.start = s
		self.finish = f
	
	# check if two tasks are compatible: 
	# i and j are compatible iff f(i) <= s(j) or f(j) <= s(i)
	def isCompatibleWith(self, t):
		return(True if (t.start >= self.finish or self.start >= t.finish) else False)

# function to remove all tasks incompatible with the current-task from consideration
def filterOutIncompatibles(tasks, t):
	filtered = []
	n = len(tasks)
	for i in range(n):
		if(t.isCompatibleWith(tasks[i])):
			filtered.append(tasks[i])
	return filtered

def main():
	# input tasks
	n = int(input("Enter the # of tasks: "))
	tasks = [None for i in range(n)]
	for i in range(n):
		print("Task #" + str(i+1) + ":")
		s = int(input("\tEnter starting-time: "))
		f = int(input("\tEnter finishing-time: "))
		if(s >= f):
			print("Invalid input!")
			return
		tasks[i] = Task(i+1, s, f)
	
	# sort the tasks in non-decreasing order of finishing-time
	tasks.sort(key = lambda x: x.finish)
	
	# perform the scheduling
	scheduled = []
	while(len(tasks) > 0):
		currentTask = tasks[0]
		scheduled.append(currentTask)
		tasks = filterOutIncompatibles(tasks, currentTask)
	
	# print the scheduled set of tasks
	print("\nScheduled tasks:")
	print("#\tSTART\tFINISH")
	for t in scheduled:
		print(str(t.id) + "\t" + str(t.start) + "\t" + str(t.finish))

main()