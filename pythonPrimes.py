def Main():
	n = input("Please enter a number: ")
	for x in range (0,n):
		if isPrime(x):
			print x

def isPrime(x):
	for i in range(2, x):
		if x%i == 0:
			return False
	return True

Main()
