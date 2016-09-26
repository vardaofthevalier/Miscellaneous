import argparse


def count_dna_nucleotides(dna_seq):
	counts = {
		"A": 0,
		"C": 0,
		"G": 0,
		"T": 0
	}

	for c in dna_seq:
		counts[c] += 1

	return counts["A"], counts["C"], counts["G"], counts["T"]

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	dna_seq = lines[0].strip()
	A, C, G, T = count_dna_nucleotides(dna_seq)

	print "{A} {C} {G} {T}".format(A=A, C=C, T=T, G=G)