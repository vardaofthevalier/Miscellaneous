#10,001st prime number

def generatePrimes(k):

	primes = [2]
	count = 2
	primesChecked = 0
	
	while len(primes) < k:
		for primeNum in primes:
			if count % primeNum != 0:
				primesChecked += 1
			
		if primesChecked == len(primes):
			primes.append(count)
		
		count += 1
		primesChecked = 0
				
	return primes	
	

def main():
	k = 10001
	
	# Generate all the prime numbers up to the limit
	primes = generatePrimes(k)
	
	# Otherwise, just print the kth prime in the list
	print "The 10001st prime number is: " + str(primes[k-1])


if __name__ == "__main__":
	main()
	