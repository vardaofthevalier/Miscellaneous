import argparse


def probability_dominant(homozygous_dominant, heterozygous, homozygous_recessive):
	denominator = (homozygous_dominant + heterozygous + homozygous_recessive)

	# P(homozygous_dominant, homozygous_dominant)
	p_hd_hd = (homozygous_dominant/float(denominator)) * ((homozygous_dominant - 1)/(float(denominator) - 1))

	# P(heterozygous, heterozygous)
	p_het_het = (heterozygous/float(denominator)) * ((heterozygous - 1)/(float(denominator) - 1))

	# P(homozygous_recessive, homozygous_recessive)
	p_hr_hr = (homozygous_recessive/float(denominator)) * ((homozygous_recessive - 1)/(float(denominator) - 1))

	# P(homozygous_dominant, heterozygous)
	p_hd_het = 2 * (homozygous_dominant/float(denominator)) * (heterozygous/(float(denominator) - 1))

	# P(homozygous_dominant, homozygous_recessive)
	p_hd_hr = 2 * (homozygous_dominant/float(denominator)) * (homozygous_recessive/(float(denominator) - 1))

	# P(heterozygous, homozygous_recessive)
	p_het_hr = 2 * (heterozygous/float(denominator)) * (homozygous_recessive/(float(denominator) - 1))

	print float(p_hd_hd + p_het_het + p_hr_hr + p_hd_het + p_hd_hr + p_het_hr)

	return (p_hd_hd + p_hd_het + p_hd_hr + 0.75 * p_het_het + 0.5 * p_het_hr)/float(p_hd_hd + p_het_het + p_hr_hr + p_hd_het + p_hd_hr + p_het_hr)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--homozygous-dominant", required=True)
	parser.add_argument("--heterozygous", required=True)
	parser.add_argument("--homozygous-recessive", required=True)

	args = parser.parse_args()

	print probability_dominant(int(args.homozygous_dominant), int(args.heterozygous), int(args.homozygous_recessive))