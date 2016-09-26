import argparse


def substring_locations(s, t):
	locations = []

	i = 0

	while i < len(s):
		if s[i:i+len(t)] == t:
			locations.append(i+1)

		i += 1

	return locations

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	args = parser.parse_args()

	with open(args.infile) as f:
		s, t = [x.strip() for x in f.readlines()]

	print ' '.join([str(x) for x in substring_locations(s, t)])

