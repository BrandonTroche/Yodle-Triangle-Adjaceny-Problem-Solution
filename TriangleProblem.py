""" Copyright (c) 2015 Apportable. All rights reserved.

	By: Brandon Troche
	Date Completed: 07/08/2016
	Github: https://github.com/BrandonTroche

	In this program I solve the triangle problem where I am supposed to add together all
	the maximum numbers down a list that are adjacent to the previous number I added. 

	I decided I needed to create an array of arrays which is what I did here with "trianglePoints."
	From there I would algorithmically loop through the multidimensional array and check the adjacent 
	spaces just like a matrix until I was finished. 

	I decided not to use "import numpy" for easier matrix creation as the size of this matrix would
	be too varying. I decided to just use simple code instead.  
"""
import sys

__author__ = "Brandon Troche"
__copyright__ = "Copyright 2016"
__maintainer__ = "Brandon Troche"
__email__ = "bttroche@gmail.com"

def main():
	triangle = open('triangle.txt', 'r')	#File i/o
	#triangle = open('test.txt', 'r')
	triangleLines = []	#Array of rows in the triangle
	trianglePoints = []		#Array of arrays of each row in the file and the points of the triangle in those rows


	for line in triangle:
		triangleLines.append(line)		#Add each row from the file into my array

	#print "___________________________"
	#print len(triangleLines)
	#print triangleLines[0]
	#print triangleLines[1]
	#print triangleLines[2]

	for index in triangleLines:
		trianglePoints.append(index.split())	#Split those rows into arrays and add those arrays of points to an array

	#print trianglePoints[0][0]
	#print trianglePoints[1][0]
	#print trianglePoints[1][1]
	#print "The sizes of trianglePoints is: "

	print "_____________________________"		#Separator for easier viewing

	total = int(trianglePoints[0][0])	#Set the total equal to the first number in the triangle since my algorithm is only for adjacent numbers
	pivotPoint = [0, 0]		#A 2-valued array keeping track of the largest adjacent number to check adjacent numbers from

	print "The beginning Pivot Point is: " + str(pivotPoint[0]) + " : " + str(pivotPoint[1])	#Show start point for debugging purposes

	#print "Size of trianglePoints: " + str(len(trianglePoints[99]))

	print "_____________________________"		#Separator for easier viewing

	for outter in range(len(trianglePoints)-1):		#Looping from 0 to 99 arrays. This is an O(N) run-time algorithm. It will run a maximum of N times where N is the size of rows in the triangle
		if pivotPoint[0] >= int(len(trianglePoints)):		#Checking our range. If we are out of range, the rest of the code will give an error and therefore we should stop
				break
		print "Adjacent Numbers -- " + str(trianglePoints[pivotPoint[0]+1][pivotPoint[1]]) + " : " + str(trianglePoints[pivotPoint[0]+1][pivotPoint[1]+1])	#Debugging purposes
		if int(trianglePoints[pivotPoint[0]+1][pivotPoint[1]]) >= int(trianglePoints[pivotPoint[0]+1][pivotPoint[1]+1]):	#If the left adjacent value is greater
			total += int(trianglePoints[pivotPoint[0]+1][pivotPoint[1]])	#Then add the left adjacent value to the total
			pivotPoint = [pivotPoint[0] + 1, pivotPoint[1]]			#and then set the pivot point to the point of the left value
			print "Pivot point: " + str(pivotPoint)		#Debugging purposes
			print "Total: " + str(total)		#Debugging purposes	
		else:		#Else: Or rather if the right adjacent value is larger instead as there are only two cases


			total += int(trianglePoints[pivotPoint[0]+1][pivotPoint[1]+1])		#Add the right value to the total
			pivotPoint = [pivotPoint[0] + 1, pivotPoint[1] + 1]		#And then set the pivot point to the point of the right value
			print "Pivot point: " + str(pivotPoint)		#Debugging purposes
			print "Total: " + str(total)	#Debugging purposes

	print "The final total is: " + str(total)		#And there's your answer. Just like magic, huh?

main()