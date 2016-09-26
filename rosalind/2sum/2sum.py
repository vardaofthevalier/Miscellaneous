import argparse


class TwoSumArrayObject(object):
	def __init__(self, value, index):
		super(TwoSumArrayObject, self).__init__()
		self.value = value
		self.index = index


def find_zero_indices(A):
	hi = None
	lo = None

	for i, e in enumerate(A):
		if e.value == 0:
			if lo is None:
				lo = i
		else:
			if lo is not None:
				hi = i - 1
				break

	return hi, lo


def two_sum(A):
	sortedA = sorted(A, cmp=lambda x, y: cmp(x.value, y.value))  # O(nlgn)

	hi, lo = find_zero_indices(sortedA)  # O(n)

	if hi is None:
		sortedA.append(TwoSumArrayObject(0, None))
		sortedA = sorted(sortedA, cmp=lambda x, y: cmp(x.value, y.value))

	hi, lo = find_zero_indices(sortedA)

	i = hi + 1 # upper incrementer
	j = lo - 1 # lower incrementer

	results = []

	while i < len(sortedA) and j >= 0:  # O(n)
		if sortedA[i].value == -1*sortedA[j].value and sortedA[i].index < sortedA[j].index:
			return sortedA[i].index, sortedA[j].index
		elif sortedA[i].value < -1*sortedA[j].value:
			i += 1
		else:
			j -= 1

	return -1


if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--sort", action="store_true", default=False)
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	arrays = [x.strip().split(' ') for x in lines[1:]]
	results = []

	for a in arrays:
		twosum = two_sum([TwoSumArrayObject(int(x), i + 1) for i, x in enumerate(a)])
		results.append(twosum)

	for r in results:
		if r == -1:
			print r
		else:
			print ' '.join([str(x) for x in list(r)])

