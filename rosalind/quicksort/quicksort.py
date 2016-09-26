import argparse


def quicksort(A):
	pass

def partition(A, x):
	i = len(A) - 1

	while i > x:
		if A[i] <= A[x]:
			v = A.pop(i)
			A.insert(0, v)
			x += 1

		else:
			i -= 1

	return A

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()


	r = partition([int(x) for x in lines[1].strip().split(' ')], 0)
	print ' '.join([str(x) for x in r])
	#print ' '.join([str(y) for y in quicksort([int(x) for x in lines[1].strip().split(' ')])])
