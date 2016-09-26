# Multiples of 3 and 5

def main():
	runningTotal = 0
	
	# Find all multiples of 3 or 5 below 1000, and add them to the total
	
	k = 1
	
	multiples = []
	
	while k * 3 < 1000:
		multiples.append(k*3)
		runningTotal += k*3
		k += 1
		
	k = 1
	
	while k * 5 < 1000:
		if k*5 not in multiples:
			runningTotal += k*5
			multiples.append(k*5)
		k += 1
	
	print "The total sum of multiples of 3 and 5 less than 1000 is: " + str(runningTotal)


if __name__ == "__main__":
	main()