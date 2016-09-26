import argparse

CODONS = {
	"UUU": "F",
	"CUU": "L",
	"AUU": "I",
	"GUU": "V",
	"UUC": "F",
	"CUC": "L",
	"AUC": "I",
	"GUC": "V",
	"UUA": "L",
	"CUA": "L",
	"AUA": "I",
	"GUA": "V",
	"UUG": "L",
	"CUG": "L",
	"AUG": "M",
	"GUG": "V",
	"UCU": "S",
	"CCU": "P",
	"ACU": "T",
	"GCU": "A",
	"UCC": "S",
	"CCC": "P",
	"ACC": "T",
	"GCC": "A",
	"UCA": "S",
	"CCA": "P",
	"ACA": "T",
	"GCA": "A",
	"UCG": "S",
	"CCG": "P",
	"ACG": "T",
	"GCG": "A",
	"UAU": "Y",
	"CAU": "H",
	"AAU": "N",
	"GAU": "D",
	"UAC": "Y",
	"CAC": "H",
	"AAC": "N",
	"GAC": "D",
	"UAA": "Stop",
	"CAA": "Q",
	"AAA": "K",
	"GAA": "E",
	"UAG": "Stop",
	"CAG": "Q",
	"AAG": "K",
	"GAG": "E",
	"UGU": "C",
	"CGU": "R",
	"AGU": "S",
	"GGU": "G",
	"UGC": "C",
	"CGC": "R",
	"AGC": "S",
	"GGC": "G",
	"UGA": "Stop",
	"CGA": "R",
	"AGA": "R",
	"GGA": "G",
	"UGG": "W",
	"CGG": "R",
	"AGG": "R",
	"GGG": "G"
}


def rna2protein(rna):
	i = 0
	j = 2

	protein = []

	while j < len(rna):
		if CODONS[rna[i:j+1]] != "Stop":
			protein.append(CODONS[rna[i:j+1]])

		else:
			break

		i = j + 1
		j = i + 2

	return ''.join(protein)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	parser.add_argument("--verify", required=False)
	args = parser.parse_args()

	with open(args.infile) as f:
		rna = f.readlines()[0].strip()

	if args.verify:
		print rna2protein(rna) == args.verify

	else:
		print rna2protein(rna)