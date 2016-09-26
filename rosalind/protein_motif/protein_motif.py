import re
import argparse
import requests
import pprint


def protein_motif(s, motif):
	locations = []

	i = 0

	while i < len(s):
		if re.match(motif, s[i:]):
			locations.append(i + 1)

		i += 1

	return locations

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	parser.add_argument("--motif", required=False, default='^N[^P][S|T][^P]')
	args = parser.parse_args()

	with open(args.infile) as f:
		protein_ids = [x.strip() for x in f.readlines()]

	for p in protein_ids:
		uniprot_url = "http://www.uniprot.org/uniprot/{protein_id}.fasta".format(protein_id=p)
		data = requests.get(uniprot_url)
		protein_string = ''.join([x for x in data.content.split('\n')[1:] if len(x) > 0])
		locations = protein_motif(p, args.motif)
		if len(locations) > 0:
			print p
			print ' '.join([str(x) for x in locations])


