import argparse


class ArrayObject(object):
	def __init__(self, value, index):
		super(ArrayObject, self).__init__()
		self.value = value
		self.index = index


def find_zero_index(A):
	zero_i = None

	for i, e in enumerate(A):
		if e.value == 0:
			zero_i = i
			break

	return zero_i

def remove_dups(A):
	i = 0
	current = A[i]
	new_A = [current]

	while i + 1 < len(A):
		if A[i + 1].value == current.value:
			if A[i+1].index < current.index:
				new_A.pop(len(A) - 1)
				current = A[i+1]
				new_A.append(current)
			else:
				pass
		else:
			current = A[i+1]
			new_A.append(current)

		i += 1

	print [x.index for x in A]
	print [x.index for x in new_A]
	return new_A


def three_sum(A):
	#A = remove_dups(sorted(A, cmp=lambda x, y: cmp(x.value, y.value)))  # O(nlgn)

	#zero_i = find_zero_index(A)  # O(n)

	#if zero_i is None:
	#	A.append(ArrayObject(0, None))
	#	A = sorted(A, cmp=lambda x, y: cmp(x.value, y.value))

	#	zero_i = find_zero_index(A)

	#i = zero_i + 1 # upper incrementer
	#j = zero_i - 1 # lower incrementer

	A = sorted(A, cmp=lambda x, y: cmp(x.value, y.value))
	j = len(A) - 1
	i = 0

	#while i < len(A) and j >= 0:
	while j > i:
		if A[j].value + A[i].value > 0:
			if A[j].value + A[i].value + A[i+1].value == 0:
				return sorted([A[j-1].index, A[j].index, A[i].index])

			elif A[j].value + A[i].value + A[i+1].value > 0:
				j -= 1

			elif A[j].value + A[i].value + A[i+1].value < 0:
				i += 1

		elif A[j].value + A[i].value < 0:
			if A[j].value + A[i].value + A[j-1].value == 0:
				return sorted([A[j].index, A[i].index, A[i+1].index])

			elif A[j].value + A[i].value + A[j-1].value > 0:
				i += 1

			elif A[j].value + A[i].value + A[j-1].value < 0:
				j -= 1

		else:
			if A[j-1].value == 0:
				return sorted([A[j].index, A[i].index, A[j - 1].index])

			elif A[i+1].value == 0:
				return sorted([A[j].index, A[i].index, A[i + 1].index])

			else:
				i += 1

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

	for i, a in enumerate(arrays):
		threesum = three_sum([ArrayObject(int(x), i + 1) for i, x in enumerate(a)])
		results.append(threesum)

	for r in results:
		if r == -1:
			print r
		else:
			print ' '.join([str(x) for x in list(r)])

