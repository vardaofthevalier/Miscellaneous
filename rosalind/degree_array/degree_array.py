import pprint
import argparse


def adjacency_matrix(edges, v):
	matrix = {}

	for e in edges:
		v1, v2 = e
		if v1 in matrix.keys():
			matrix[v1].append(v2)

		else:
			matrix[v1] = [v2]

		if v2 in matrix.keys():
			matrix[v2].append(v1)

		else:
			matrix[v2] = [v1]

	if v > len(matrix.keys()):
		diff = v - len(matrix.keys())
		while diff > 0:
			matrix[max(matrix.keys()) + 1] = []
			diff -= 1

	return matrix


def degree_array(edges, v):
	degrees = {}
	for e in edges:
		v1, v2 = e
		if v1 in degrees.keys():
			degrees[v1] += 1
		
		else:
			degrees[v1] = 1
			
		if v2 in degrees.keys():
			degrees[v2] += 1
			
		else:
			degrees[v2] = 1

	if v > len(degrees.keys()):
		diff = v - len(degrees.keys())
		while diff > 0:
			degrees[max(degrees.keys()) + 1] = 0
			diff -= 1
	
	#pprint.pprint(degrees)
			
	return [x for x in degrees.itervalues()]

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--double", action="store_true", default=False)
	args = p.parse_args()
	
	with open(args.infile) as f:
		lines = f.readlines()
		
	edge_list = [(int(x.strip().split(' ')[0]), int(x.strip().split(' ')[1])) for x in lines[1:]]

	total_v, _ = [int(x) for x in lines[0].strip().split(' ')]
	d = degree_array(edge_list, total_v)

	if args.double:
		adjacency_matrix = adjacency_matrix(edge_list, total_v)
		#pprint.pprint(adjacency_matrix)
		double_degree_array = []

		for v, neighbors in adjacency_matrix.iteritems():
			s = 0
			for n in neighbors:
				s += d[n-1]

			double_degree_array.append(s)

		print ' '.join([str(x) for x in double_degree_array])
	else:
		print ' '.join([str(x) for x in d])
