import argparse


def majority_element(A):
	counts = {}
	for element in A:
		if element in counts.keys():
			if counts[element] + 1 > len(A)/2:
				return element

			counts[element] += 1

		else:
			counts[element] = 1

	return -1

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--double", action="store_true", default=False)
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	arrays = [x.strip().split(' ') for x in lines[1:]]
	majority_elements = []

	for a in arrays:
		majority_elements.append(majority_element(a))

	print ' '.join([str(x) for x in majority_elements])

