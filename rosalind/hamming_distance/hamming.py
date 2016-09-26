import argparse


def hamming_distance(s, t):
	count = 0
	d = 0

	while count < len(s):
		if s[count] != t[count]:
			d += 1

		count += 1

	return d

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	args = parser.parse_args()

	with open(args.infile) as f:
		strands = f.readlines()

	print hamming_distance(strands[0].strip(), strands[1].strip())