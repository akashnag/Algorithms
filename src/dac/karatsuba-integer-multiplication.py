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
# Given two arbitrarily large N digit integers. Use the Karatsuba algorithm
# to multiply them.

# Running-time: O(n^1.58)

import math

def divide(x):
	n = len(x)
	k = n//2
	if(k & (k-1) != 0):
		x1 = x[0:k+1]
		x0 = x[k+1:]
	else:
		x1 = x[0:k]
		x0 = x[k:]
	return(x1,x0)

def zFill(x,n):
	if(len(x)<n):
		d = n - len(x)
		for i in range(d):
			x = "0" + x
	return x

def shiftLeft(x,n):
	for i in range(n):
		x = x + "0"
	return x

def equalize(x,y):
	m = len(x)
	n = len(y)
	mlen = m if(m>n) else n
	for i in range(mlen-m):
		x = "0" + x
	for i in range(mlen-n):
		y = "0" + y
	return(x,y)	

def tensComplement(x):
	n = len(x)
	z = ""
	for i in range(n):
		z = z + str(9 - int(x[i]))
	return add(z,"1")

def sub(x,y):
	(x,y)=equalize(x,y)
	n=len(x)
	z=add(x,tensComplement(y))
	if(len(z) > n): z = z[1:]
	return z

def add(x,y):
	(x,y)=equalize(x,y)
	z=""
	n=len(x)
	carry=0
	sum=0
	for i in range(n-1,-1,-1):
		sum = int(x[i]) + int(y[i]) + carry
		carry = sum // 10
		sum = sum % 10
		z = str(sum) + z
	if(carry > 0): z = str(carry) + z
	return z

def mul(x,y):
	if(len(x)==1 or len(y)==1):
		return str(int(x) * int(y))
	else:
		(x,y) = equalize(x,y)
		n = len(x)
	
		(x1,x0) = divide(x)
		(y1,y0) = divide(y)
		#print(x0+","+x1+","+y0+","+y1)
		z0 = mul(x0,y0)
		z2 = mul(x1,y1)
		z1a = add(x0,x1)
		z1b = add(y0,y1)
		z1c = mul(z1a,z1b)
		z1d = sub(z1c,z0)
		z1 = sub(z1d,z2)
		za = shiftLeft(z2,n)
		zb = shiftLeft(z1,n//2)
		zc = add(za,zb)
		z = add(zc,z0)
		return z

def main():
	n = int(input("Enter the # of digits in your numbers (power of 2): "))
	if((n & (n-1)) != 0):
		print("Sorry, it must be a power of 2")
		return

	x = input("Enter the 1st " + str(n) + "-digit number: ")
	y = input("Enter the 2nd " + str(n) + "-digit number: ")
	
	if(n != len(x) or n != len(y)):
		print("# of digits unequal to " + str(n) + "!")
		return

	z=mul(x,y)
	print("\nProduct: " + z)

main()