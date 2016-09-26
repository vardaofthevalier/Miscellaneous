import argparse
import pprint


def read_fasta(f):
	strands = {x.split('\r\n')[0]: ''.join(x.split('\r\n')[1:]) for x in f.read().strip().split('>') if len(x) > 0}

	return strands

def compute_gc_content(strand):
	total_gc = 0
	total = 0

	for c in strand:
		if c == "G" or c == "C":
			total_gc += 1

		total += 1

	return 100 * total_gc/float(total)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")

	args = parser.parse_args()

	with open(args.infile) as f:
		strands = read_fasta(f)

	#pprint.pprint(strands)
	#exit(0)

	current_max_label = None
	current_max_value = 0

	for s in strands.keys():
		v = compute_gc_content(strands[s])
		if v > current_max_value:
			current_max_value = v
			current_max_label = s

	print "{label}\n{gc_content}".format(label=current_max_label, gc_content=current_max_value)