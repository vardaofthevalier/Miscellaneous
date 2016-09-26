import math
import argparse


def n_choose_k(n, k):
	return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

def independent_alleles(k, N):
	p_N = 0.25

	return sum([(0.25**x)*(0.75**(2**k - x))*n_choose_k(2**k, x) for x in range(N, 2**k + 1)])

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--k", required=True)
	parser.add_argument("--N", required=True)

	args = parser.parse_args()

	print str(independent_alleles(int(args.k), int(args.N)))