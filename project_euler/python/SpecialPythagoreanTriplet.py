#Special Pythagorean triplet:

def main():
	a = 1
	b = 2
	c = 997
	
	foundTriplet = False
	triplet = None;
	
	loopCount = 0
	
	while a < b and foundTriplet == False:
		while b < c:
			if a*a + b*b == c*c:
				foundTriplet = True
				triplet = (a, b, c)
				break
			b += 1
			c = 1000 - (a + b)
			loopCount += 1
		a += 1
		b = a + 1
		c = 1000 - (a + b)
	
	if foundTriplet == False:
		print "No Special Pythagorean triplet was found."
	else:
		a, b, c = triplet
		print "a = " + str(a)
		print "b = " + str(b)
		print "c = " + str(c)
		print "abc = " + str(a*b*c)
		print "loops = " + str(loopCount)
		

if __name__ == "__main__":
	main()
	