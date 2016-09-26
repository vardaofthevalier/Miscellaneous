import math
import argparse


def max_heapify_array(A):
	H = []

	while len(A) > 0:
		i = A.pop(0)
		H.append(i)

		if len(H) == 1:
			continue

		else:
			j = len(H) - 1

			while H[j] > H[int(math.ceil(j/2.0)) - 1] and j > 0:
				#print "Before swap: " + str(H)
				#print j
				#print int(math.ceil(j / 2.0)) - 1
				H_j = H[j]
				H[j] = H[int(math.ceil(j/2.0)) - 1]
				H[int(math.ceil(j/2.0)) - 1] = H_j
				#print "After swap: " + str(H)

				j = int(math.ceil(j/2.0)) - 1

	return H

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")

	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	A = [int(x) for x in lines[1].split(' ')]

	H = max_heapify_array(A)

	print ' '.join([str(x) for x in H])