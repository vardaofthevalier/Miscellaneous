import argparse


def dna2rna(rna_seq):
	dna_seq = []

	for c in rna_seq:
		if c == "T":
			dna_seq.append("U")
		else:
			dna_seq.append(c)

	return ''.join(dna_seq)

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--verify")
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	rna_seq = lines[0].strip()

	if args.verify:
		print dna2rna(rna_seq) == args.verify

	else:
		print dna2rna(rna_seq)
