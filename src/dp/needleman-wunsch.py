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
# Given two DNA sequences of lengths M and N, find the optimal alignment.

# Running-time: O(m.n)

scoringMatrix = [
		[ 0, -1, -1, -1, -1 ],
		[ -1, 1, 0, 0, 0 ],
		[ -1, 0, 1, 0, 0 ],
		[ -1, 0, 0, 1, 0 ],
		[ -1, 0, 0, 0, 1 ]
	]

indexMap = {
	"-": 0, "A": 1, "T": 2, "G": 3, "C": 4
}

def getScore(a,b):
	return scoringMatrix[indexMap[a]][indexMap[b]]

class TableEntry:
	def __init__(self, score, direction):
		self.score = score
		self.dir = direction

def isInputValid(s1, s2, m, n):
	nuc = [ 'A', 'T', 'G', 'C' ]
	for i in range(m):
		if(s1[i] not in nuc):
			return False
	for i in range(n):
		if(s2[i] not in nuc):
			return False
	return True

def main():
	s1 = input("Enter the 1st DNA sequence: ")
	s2 = input("Enter the 2nd DNA sequence: ")
	
	#s1 = "ACAGTAG"
	#s2 = "ACTCG"

	s1 = s1.upper().strip()
	s2 = s2.upper().strip()
	
	m = len(s1)
	n = len(s2)

	if(not isInputValid(s1,s2,m,n)):
		print("Invalid DNA sequence!")
		return

	dp = [ None for i in range(m+1)]
	for i in range(m+1):
		dp[i] = [ None for j in range(n+1)]
	
	dp[0][0] = TableEntry(getScore("-","-"), "n")
	for i in range(1,m+1):
		dp[i][0] = TableEntry(dp[i-1][0].score + getScore(s1[i-1], "-"), "u")
	for i in range(1,n+1):
		dp[0][i] = TableEntry(dp[0][i-1].score + getScore(s2[i-1], "-"), "l")

	for i in range(1,m+1):
		for j in range(1,n+1):
			c1 = s1[i-1]
			c2 = s2[j-1]

			score1 = dp[i][j-1].score + getScore(c1,"-")
			score2 = dp[i-1][j].score + getScore("-",c2)
			score3 = dp[i-1][j-1].score + getScore(c1,c2)

			if(score1 > score2 and score1 > score3):
				dp[i][j] = TableEntry(score1, "l")
			elif(score2 > score1 and score2 > score3):
				dp[i][j] = TableEntry(score2, "u")
			else:
				dp[i][j] = TableEntry(score3, "d")
	
	i = m
	j = n
	x = ""
	y = ""
	while(dp[i][j].dir != "n"):
		dir = dp[i][j].dir
		if(dir == "d"):
			x = s1[i-1] + x
			y = s2[j-1] + y
			i = i - 1
			j = j - 1
		elif(dir=='u'):
			x = s1[i-1] + x
			y = "-" + y
			i = i - 1
		elif(dir=='l'):
			x = "-" + x
			y = s2[j-1] + y
			j = j - 1

	print("\nAligned sequences: ")
	print(x)
	print(y)

main()