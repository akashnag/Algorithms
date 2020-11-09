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
# Given two N x N matrices, multiply them using Strassen's algorithm.

# Running-time: O(n^2.8)

class SubMatrix:
	def __init__(self, matrix, n, rowStart, rowEnd, colStart, colEnd):
		self.matrix = matrix
		self.n = n
		self.rs = rowStart
		self.re = rowEnd
		self.cs = colStart
		self.ce = colEnd

	def set(self, submat):
		for r in range(self.rs, self.re+1):
			for c in range(self.cs, self.ce+1):
				self.matrix[r][c] = submat.getElement(r-self.rs, c-self.cs)

	def order(self):
		return self.re - self.rs + 1

	def getElement(self, i, j):
		return self.matrix[self.rs+i][self.cs+j]
	
	def setElement(self, i, j, v):
		self.matrix[self.rs+i][self.cs+j] = v

	def display(self):
		for i in range(self.rs, self.re+1):
			for j in range(self.cs, self.ce+1):
				print(self.matrix[i][j], end='\t')
			print()

def createMatrix(n):
	x = [0 for i in range(n)]
	for i in range(n):
		x[i] = [0 for j in range(n)]
	return x

def createSubMatrix(n):
	x = createMatrix(n)
	return(SubMatrix(x,n,0,n-1,0,n-1))

def addSub(sm1, sm2, sub=False):
	n = sm1.re - sm1.rs + 1
	res = createMatrix(n)
	for r in range(n):
		for c in range(n):
			m = -1 if sub else 1
			res[r][c] = sm1.getElement(r,c) + (m * sm2.getElement(r,c))
	return(SubMatrix(res,n,0,n-1,0,n-1))

def multiply(a,b,c):
	n = a.order()
	if(n == 1):
		p = a.getElement(0,0) * b.getElement(0,0)
		c.setElement(0,0,p)
	else:
		arm = (a.rs + a.re) // 2
		acm = (a.cs + a.ce) // 2
		a11 = SubMatrix(a.matrix, a.n, a.rs, arm, a.cs, acm)
		a12 = SubMatrix(a.matrix, a.n, a.rs, arm, acm+1, a.ce)
		a21 = SubMatrix(a.matrix, a.n, arm+1, a.re, a.cs, acm)
		a22 = SubMatrix(a.matrix, a.n, arm+1, a.re, acm+1, a.ce)

		brm = (b.rs + b.re) // 2
		bcm = (b.cs + b.ce) // 2
		b11 = SubMatrix(b.matrix, b.n, b.rs, brm, b.cs, bcm)
		b12 = SubMatrix(b.matrix, b.n, b.rs, brm, bcm+1, b.ce)
		b21 = SubMatrix(b.matrix, b.n, brm+1, b.re, b.cs, bcm)
		b22 = SubMatrix(b.matrix, b.n, brm+1, b.re, bcm+1, b.ce)
		
		crm = (c.rs + c.re) // 2
		ccm = (c.cs + c.ce) // 2
		c11 = SubMatrix(c.matrix, c.n, c.rs, crm, c.cs, ccm)
		c12 = SubMatrix(c.matrix, c.n, c.rs, crm, ccm+1, c.ce)
		c21 = SubMatrix(c.matrix, c.n, crm+1, c.re, c.cs, ccm)
		c22 = SubMatrix(c.matrix, c.n, crm+1, c.re, ccm+1, c.ce)
		
		m1 = createSubMatrix(n//2)
		m2 = createSubMatrix(n//2)
		m3 = createSubMatrix(n//2)
		m4 = createSubMatrix(n//2)
		m5 = createSubMatrix(n//2)
		m6 = createSubMatrix(n//2)
		m7 = createSubMatrix(n//2)
		
		multiply(addSub(a11,a22), addSub(b11,b22), m1)
		multiply(addSub(a21,a22), b11, m2)
		multiply(a11, addSub(b12, b22, True), m3)
		multiply(a22, addSub(b21, b11, True), m4)
		multiply(addSub(a11, a12), b22, m5)
		multiply(addSub(a21, a11, True), addSub(b11, b12), m6)
		multiply(addSub(a12, a22, True), addSub(b21, b22), m7)

		c11.set(addSub(addSub(addSub(m1,m4), m5, True), m7))
		c12.set(addSub(m3,m5))
		c21.set(addSub(m2,m4))
		c22.set(addSub(addSub(addSub(m1,m2,True),m3),m6))

def main():
	n = int(input("Enter the order of the matrices (must be a power of 2): "))
	if(n<=0 or (n & (n-1)) != 0):
		print("Invalid order")
		return

	a = createSubMatrix(n)
	b = createSubMatrix(n)
	c = createSubMatrix(n)

	print("Enter elements in the 1st matrix:")
	for i in range(n):
		for j in range(n):
			a.matrix[i][j] = int(input("\tEnter element at position(" + str(i) + "," + str(j) + "): "))

	print("\nEnter elements in the 2nd matrix:")
	for i in range(n):
		for j in range(n):
			b.matrix[i][j] = int(input("\tEnter element at position(" + str(i) + "," + str(j) + "): "))

	multiply(a,b,c)
	print("\nProduct Matrix: ")
	c.display()

main()