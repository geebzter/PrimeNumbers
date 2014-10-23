#title		:pythonPrimes.py
#author		:Alex Ciaramella
#date		:10/22/14
#usage		:python pythonPrimes.py

#Main:
#	Prompts user to enter a number and then loops
#	from 0 to the entered number, checking if each 
#	intermediate number in the range is prime.
#	If so, print out that number

from math import sqrt

def Main():
	#Retrieve input from user
	n = input("Please enter a number: ")

	#Loop from 0 to entered number
	for x in range (0,n+1):
		#check if number is prime
		if isPrime(x):
			print x

#isPrime(x):
#	@param: an integer
#	@return: True if the parameter is prime
#		 False if the parameter is composite
def isPrime(x):
	#0, 1, and negative integers are not prime
	if x < 2:
		return False

	lastdivisor = int(sqrt(x))

	#loop from 2 to the last possible divisor
	for i in range(2, lastdivisor+1):
		#if x  is evenly divisible(no remainder)
		#by any number i < x, then it is not prime
		#therefore return false 
		if x%i == 0:
			return False

	#x must only be evenly divisble by itself and 1
	#and must be prime
	#therefore return True 

	return True

#Call the main function when starting the program
Main()
