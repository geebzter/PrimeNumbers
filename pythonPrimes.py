def Main():
	n = input("Please enter a number: ")
	for x in range (0,n):
		if isPrime(x):
			print x

def isPrime(x):
	if x < 2:
		return False

	for i in range(2, x):
		if x%i == 0:
			return False
	return True

Main()
