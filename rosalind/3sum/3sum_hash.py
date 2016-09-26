import argparse


def three_sum(A):
	h = {}

	for i, e in enumerate(A):
		try:
			idx = h[e]

		except KeyError:
			h[e] = i

	i = 0

	while i < len(A) - 1:
		j = i + 1

		while j < len(A):
			try:
				idx = h[-1*(A[i] + A[j])]

			except KeyError:
				pass

			else:
				return sorted([i + 1, j + 1, idx + 1])

			j += 1

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
		threesum = three_sum([int(x) for x in a])
		results.append(threesum)

	for r in results:
		if r == -1:
			print r
		else:
			print ' '.join([str(x) for x in list(r)])

