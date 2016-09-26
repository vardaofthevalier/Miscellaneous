import argparse


def mergesort(A):
	if len(A) > 1:
		l = mergesort(A[0:len(A)/2])
		r = mergesort(A[len(A)/2:])

		return merge(l, r)

	else:
		return A

def merge(a1, a2):
	i = 0
	j = 0

	merged = []

	while len(a1) > 0 and len(a2) > 0:
		if a1[0] < a2[0]:
			merged.append(a1.pop(0))

		elif a2[0] < a1[0]:
			merged.append(a2.pop(0))

		else:
			merged.append(a1.pop(0))
			merged.append(a2.pop(0))

	if len(a1) == 0:
		merged.extend(a2)

	if len(a2) == 0:
		merged.extend(a1)

	return merged

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	print ' '.join([str(y) for y in mergesort([int(x) for x in lines[1].strip().split(' ')])])
