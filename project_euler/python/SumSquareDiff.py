def main():
	print "The difference between the sum of squares and square of sums of the first 100 natural numbers is: " + str(abs(sumOfSquares(100) - squareOfSums(100)))

def sumOfSquares(n):
	sum = 0;
	
	for num in range(n + 1):
		square = num*num
		sum += square
		
	return sum


def squareOfSums(n):
	sum = 0;
	
	for num in range(n + 1):
		sum += num;
	
	return sum*sum


if __name__ == "__main__":
	main()