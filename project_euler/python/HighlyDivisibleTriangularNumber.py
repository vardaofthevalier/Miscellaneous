# Highly divisible triangular number
from math import *
def main():
	divisors = 0
	currentNaturalNum = 1
	triangleNum = 1
	
	triangleNumsAndFactors = {1:1}
	
	# Start generating and storing triangle numbers
	while divisors <= 500:
		currentNaturalNum += 1
		triangleNum += currentNaturalNum
		divisors = numFactors(triangleNum, triangleNumsAndFactors)
	
	print "The first triangleNumber with over 500 divisors is: " + triangleNum

	
def numFactors(n, triangleNumsAndFactors):
	factors = 0
	upperBound = int(floor(n/2)) + 1)
	
	while upperBound > 0:
		if upperBound in triangleNumsAndFactors.keys():
			pass
		
		else		
			if n % upperBound == 0:
				factors.append(num)
		
		upperBound -= 1
	
	return factors
		
if __name__ == "__main__":
	main()