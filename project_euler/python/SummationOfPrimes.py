def findPrimes(numberToTest):
	upperBound = numberToTest
	primes = []
	
	# First, generate a list of odd numbers up to the upper bound 
	for num in range (2, upperBound):
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
	
	return primes

def ApplySieve(p, nextPrimeIndex, primes):
	primeMultiplesRemoved = 0
	
	loopCount = nextPrimeIndex
	while loopCount < len(primes):
		if primes[loopCount] != p and primes[loopCount] % p == 0:
			primes.pop(loopCount)
			primeMultiplesRemoved += 1
		loopCount += 1
	
	return primeMultiplesRemoved

	
def calculateSum(primes):
	# Add 2 back to the list before returning
	return sum(primes) + 2


def main():
	numberToTest = 2000000
	
	primes = findPrimes(numberToTest)
	sum = calculateSum(primes)
	
	print "The sum of all prime numbers less than 2 million is: " + str(sum)


if __name__ == "__main__":
	main()