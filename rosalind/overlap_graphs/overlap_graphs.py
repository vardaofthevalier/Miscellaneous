import argparse
import pprint
from gc_content import gc_content


def overlap_graph(k, strands):
	metadata = {label: {"prefix": dnastring[0:k], "suffix": dnastring[-k:]} for label, dnastring in strands.iteritems()}

	adj = {label: [] for label in strands.keys()}

	for s, v in metadata.iteritems():
		for t, u in metadata.iteritems():
			if s == t:
				pass
			else:
				if v["suffix"] == u["prefix"]:
					adj[s].append(t)

	return adj

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	parser.add_argument("--k", required=True)
	args = parser.parse_args()

	with open(args.infile) as f:
		strands = gc_content.read_fasta(f)

	adj_list = overlap_graph(int(args.k), strands)

	for k, v in adj_list.iteritems():
		for neighbor in v:
			print "{k} {neighbor}".format(k=k, neighbor=neighbor)