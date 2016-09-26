import argparse

def dna_reverse_complement(dna_seq):
	d = [x for x in dna_seq]
	complements = {
		"A": "T",
		"T": "A",
		"C": "G",
		"G": "C"
	}

	i = 0
	j = len(d) - 1

	while j >= i:
		t = complements[d[i]]
		d[i] = complements[d[j]]
		d[j] = t

		i += 1
		j -= 1

	return ''.join(d)


if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--verify")
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	dna_seq = lines[0].strip()

	if args.verify:
		print dna_reverse_complement(dna_seq) == args.verify

	else:
		print dna_reverse_complement(dna_seq)