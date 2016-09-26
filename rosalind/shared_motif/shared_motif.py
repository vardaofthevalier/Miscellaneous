import argparse
import pprint
from gc_content import gc_content
from pyspark import SparkContext, SparkConf, AccumulatorParam


def longest_common_substring(strands):
	pass
	# create the Spark context
	conf = SparkConf().setAppName("longest_common_substring")
	sc = SparkContext(conf=conf)

	# create an accumulator for key-value pairs, where each key is a substring, and each value is the set of strings where the substring can be found
	class ArrayAccumulatorParam(AccumulatorParam):
		def zero(self, initialValue):
			return initialValue

		def addInPlace(self, v1, v2):
			if type(v2) is list:
				v1.extend(v2)
			elif type(v2) is tuple:
				v1.append(v2)

			return v1

	acc = sc.accumulator([], ArrayAccumulatorParam())

	def generate_substrings(data_element):
		k, v = data_element
		i = 0
		while i < len(v):
			j = i + 1
			while j < len(v):
				acc.add((v[i:j],k))
				j += 1
			i += 1

	sc.parallelize([(k, v) for k, v in strands.iteritems()]).foreach(generate_substrings)

	all_substrings = sc.parallelize(acc.value)
	return all_substrings.groupByKey().filter(lambda x: set(list(x[1])) == set(strands.keys())).takeOrdered(1, key=lambda x: -len(x[0]))[0][0]

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile")
	args = parser.parse_args()

	with open(args.infile) as f:
		strands = gc_content.read_fasta(f)

	print longest_common_substring(strands)