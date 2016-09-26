import argparse
import pprint


def two_sum(A):
	h = {}

	for i, e in enumerate(A):
		try:
			neg_idx = h[-1*e]

		except KeyError:
			pass

		else:
			return neg_idx, i

		try:
			idx = h[e]

		except KeyError:
			h[e] = i

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
		twosum = two_sum([int(x) for x in a])
		results.append(twosum)

	for r in results:
		if r == -1:
			print r
		else:
			print '{lo} {hi}'.format(lo=r[0] + 1, hi=r[1] + 1)

