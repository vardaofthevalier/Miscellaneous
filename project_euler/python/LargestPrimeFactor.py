# Largest Prime Factor
from math import *
from multiprocessing import *
import time

def findPrimes(numberToTest):
	upperBound = int(floor(sqrt(numberToTest)))
	primes = []
	
	# First, generate a list of odd numbers up to the upper bound 
	for num in range (2, upperBound + 1):
		if num % 2 != 0:
			primes.append(num)
		
	# Sieve of Eratosthenese: Remove multiples of each successive prime until nothing else can be removed from the list
	
	p = 3
	nextPrimeIndex = 0
	primeMultiplesRemoved = ApplySieve(p, nextPrimeIndex, primes)
	
	nextPrimeIndex = 1
	while primeMultiplesRemoved > 0:
		p = primes[nextPrimeIndex]
		primeMultiplesRemoved = ApplySieve(p, nextPrimeIndex, primes)
		nextPrimeIndex += 1
		
	# Sort the list of primes from highest to lowest.
	primes.sort()
	primes.reverse()
	
	return primes


def findLargestPrimeFactor(numberToTest, primes):		
	# Iterate over list of primes until a factor of the number is found.
	
	for num in primes:
		if numberToTest % num == 0:
			largestPrimeFactor = num
			break
	
	return largestPrimeFactor
		

def ApplySieve(p, nextPrimeIndex, primes):
	primeMultiplesRemoved = 0
	
	loopCount = nextPrimeIndex
	while loopCount < len(primes):
		if primes[loopCount] != p and primes[loopCount] % p == 0:
			primes.pop(loopCount)
			primeMultiplesRemoved += 1
		loopCount += 1
	
	return primeMultiplesRemoved
	
	
def main():
	numberToTest = 600851475143
	primes = findPrimes(numberToTest)
	largestPrimeFactor = findLargestPrimeFactor(numberToTest, primes)
	
	print "The largest prime factor of " + str(numberToTest) + " is: " + str(largestPrimeFactor)
	

if __name__ == "__main__":
	main()