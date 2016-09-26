import argparse


def expected_offspring(scaling_factor):
	ex_i = [2, 2, 2, 1.5, 1, 0]

	return sum(map(lambda x,y: x*y, x_i, ex_i))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")

	args = parser.parse_args()

	with open(args.infile) as f:
		x_i = [int(x.strip()) for x in f.read().split(' ')]

	e_x = expected_offspring(x_i)

	print e_x
