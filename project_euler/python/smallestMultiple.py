# Smallest multiple
from math import *

def main():
	runningTotal = 1
	maxMultiple = 20
	lowerBound = int(floor(maxMultiple/2))
	
	exclude = findFactors(maxMultiple)
	runningTotal *= maxMultiple
	maxMultiple -= 1
	
	while maxMultiple > lowerBound:
		if maxMultiple in exclude:
			pass
		else:
			print "Max Multiple = " + str(maxMultiple)
			print "Running total = " + str(runningTotal) + " * " + str(maxMultiple) + " = " + str(runningTotal*maxMultiple)
			runningTotal *= maxMultiple
			factors = findFactors(maxMultiple)
			
			for factor1 in factors:
				for factor2 in exclude:
					if factor1*factor2 not in exclude and (factor1*factor2) <= maxMultiple:
						print "We need to exclude: " + str(factor1*factor2)
						exclude.append(factor1*factor2)
						
		maxMultiple -= 1
	
	print "The smallest positive number that can be divided evenly by all numbers in range [1, 20] is: " + str(runningTotal)

def findFactors(n):
	factors = []
	
	print "Factors of " + str(n) + ": " 
	for num in range (2, int(floor(n/2)) + 1):
		if n % num == 0:
			print num
			factors.append(num)
	
	return factors
	
if __name__ == "__main__":
	main()