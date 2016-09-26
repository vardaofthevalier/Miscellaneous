import argparse
from gc_content import gc_content


def profile_matrix(strands):
	matrix = {
		"A": [],
		"C": [],
		"G": [],
		"T": []
	}
	consensus = []
	count = 0
	while count < len(strands[0]):
		a = 0
		c = 0
		g = 0
		t = 0
		max = 0
		maxChar = None
		for s in strands:
			if s[count] == "A":
				a += 1
				if a > max:
					max = a
					maxChar = "A"

			elif s[count] == "C":
				c += 1
				if c > max:
					max = c
					maxChar = "C"

			elif s[count] == "G":
				g += 1
				if g > max:
					max = g
					maxChar = "G"

			elif s[count] == "T":
				t += 1
				if t > max:
					max = t
					maxChar = "T"

		matrix["A"].append(a)
		matrix["C"].append(c)
		matrix["G"].append(g)
		matrix["T"].append(t)

		consensus.append(maxChar)

		count += 1

	return matrix, ''.join([str(x) for x in consensus])

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	args = parser.parse_args()

	with open(args.infile) as f:
		strands = gc_content.read_fasta(f)

	pm, consensus = profile_matrix([x for x in strands.itervalues()])

	print consensus
	print "A: {s}".format(s=' '.join([str(x) for x in pm["A"]]))
	print "C: {s}".format(s=' '.join([str(x) for x in pm["C"]]))
	print "G: {s}".format(s=' '.join([str(x) for x in pm["G"]]))
	print "T: {s}".format(s=' '.join([str(x) for x in pm["T"]]))

