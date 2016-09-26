import argparse


def rabbits(n, k, m=None):
	solutions = {
		1: 1,
		2: 1
	}

	count = 3

	while count <= n:
		if m is None or m is not None and m >= count:
			solutions[count] = solutions[count-1] + k*solutions[count-2]

		elif m is not None and m < count:
			i = count - m
			solutions[count] = solutions[count-1] + k*solutions[count-2] - solutions[i]
			births = solutions[i]
			while i < count:
				solutions[i] -= births
				i += 1

		count += 1

	return solutions[n]

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--months", required=True)
	parser.add_argument("--litter-size", required=True)
	parser.add_argument("--lifespan", required=False)

	args = parser.parse_args()

	if args.lifespan:
		print "Total rabbit pairs after {n} months: {r}".format(n=args.months, r=str(rabbits(int(args.months), int(args.litter_size), m=int(args.lifespan))))

	else:
		print "Total rabbit pairs after {n} months: {r}".format(n=args.months, r=str(rabbits(int(args.months), int(args.litter_size))))