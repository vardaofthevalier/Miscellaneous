from math import *

def main():
	largestPalindrome = None;
	
	for m in range(100, 1000):
		for n in range(100, 1000):
			if isPalindrome(m*n) and m*n > largestPalindrome:
				largestPalindrome = m*n
	print "The largest palindrome product of 3-digit numbers is: " + str(largestPalindrome)


def isPalindrome(n):
	headPosition = 0
	tailPosition = -1
	palindrome = True
	
	while headPosition < floor(len(str(n))/2):
		if int(str(n)[headPosition]) != int(str(n)[tailPosition]):
			palindrome = False
			break
		else:
			headPosition+=1
			tailPosition-=1
	
	return palindrome


if __name__ == "__main__":
    main()