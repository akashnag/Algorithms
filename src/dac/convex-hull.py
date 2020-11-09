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
# Given a set of N points, find the convex hull.

# Running-time: O(n.lg(n))
# Using Divide-and-Conquer strategy

import math

centeroid = None

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

def getCenteroid(points):
	minX = points[0].x
	minY = points[0].y
	maxX = minX
	maxY = minY

	n = len(points)
	for i in range(1,n):
		p = points[i]
		if(p.x < minX): minX=p.x
		if(p.x > maxX): maxX=p.x
		if(p.y < minY): minY=p.y
		if(p.y > maxY): maxY=p.y

	return(Point( (minX+maxX)/2, (minY+maxY)/2 ))

def radianToDegree(angle):
	deg = ((180 * angle) / math.pi)
	if(deg < 0): deg = 360 + deg
	return deg

def getAngle(point):
	return radianToDegree(math.atan2(point.y - centeroid.y, point.x - centeroid.x))
	
def sortClockwise(points):
	global centeroid
	centeroid = getCenteroid(points)
	points.sort(key=getAngle)

def intOrd(p, q, sep):
	slope = (q.y - p.y)/(q.x - p.x)
	intercept = p.y - (slope * p.x)
	return((slope * sep) + intercept)

def findTangent(hullLeft, hullRight, sep, upper=True):
	m = len(hullLeft)
	n = len(hullRight)
	i = 0
	j = 0
	while(True):
		if(upper):
			if(intOrd(hullLeft[i],hullRight[(j+1)%n],sep) >= intOrd(hullLeft[i],hullRight[j],sep)):
				j = (j+1) % n
			elif(intOrd(hullLeft[(i-1)%m],hullRight[j],sep) >= intOrd(hullLeft[i],hullRight[j],sep)):
				i = (i-1) % m
			else:
				break
		else:
			if(intOrd(hullLeft[i],hullRight[(j-1)%n],sep) <= intOrd(hullLeft[i],hullRight[j],sep)):
				j = (j-1) % n
			elif(intOrd(hullLeft[(i+1)%m],hullRight[j],sep) <= intOrd(hullLeft[i],hullRight[j],sep)):
				i = (i+1) % m
			else:
				break

	return (i,j)

def mergeHulls(hullLeft, hullRight, separator):
	sortClockwise(hullLeft)
	sortClockwise(hullRight)
	
	m = len(hullLeft)
	n = len(hullRight)

	(upperLeft, upperRight) = findTangent(hullLeft, hullRight, separator, True)
	(lowerLeft, lowerRight) = findTangent(hullLeft, hullRight, separator, False)
	
	hull = list()
	i = upperLeft
	while(True):
		hull.append(hullLeft[i])
		if(i == lowerLeft):
			break
		else:
			i = (i + 1) % m
	
	j = upperRight
	while(True):
		hull.append(hullRight[j])
		if(j == lowerRight):
			break
		else:
			j = (j - 1) % n
	
	return hull

def convexHull(points):
	n = len(points)
	if(n <= 3):
		return points
	else:
		points.sort(key = lambda p: p.x)
		lowX = points[0].x
		highX = points[n-1].x
		midX = (lowX + highX) // 2

		(left, right) = filter(points, midX)
		chLeft = convexHull(left)
		chRight = convexHull(right)
		return mergeHulls(chLeft, chRight, midX)

def filter(points, separator):
	left = list()
	right = list()

	for p in points:
		if(p.x <= separator):
			left.append(p)
		else:
			right.append(p)
	
	return (left,right)

def main():
	n = int(input("How many points? "))

	points = [ None for i in range(n) ]
	for i in range(n):
		print("Point #" + str(i+1) + ":")
		x = int(input("\tX = "))
		y = int(input("\tY = "))
		points[i] = Point(x,y)

	#n = 6
	#points = [
	#	Point(2,2), Point(10,2),
	#	Point(2,10), Point(10,10),
	#	Point(5,5), Point(7,7)
	#]

	ch = convexHull(points)

	print("\nPoints on the Convex Hull: ")
	for point in ch:
		print(str(point))

main()