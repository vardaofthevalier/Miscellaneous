import argparse
import pprint

from Queue import Queue


def adjacency_matrix(edges, directed=False):
	def count_vertices(edges):
		vertices = {}
		for e in edges:
			v1, v2 = e

			if v1 not in vertices.keys():
				vertices[v1] = 1

			if v2 not in vertices.keys():
				vertices[v2] = 1

		return len(vertices.keys())

	v = count_vertices(edges)

	matrix = [[0 for x in range(1, v+1)] for y in range(1, v+1)]

	for e in edges:
		v1_id, v2_id = e

		if v1_id == v2_id:
			print "ERROR: self loop!"
			exit(0)

		matrix[v1_id][v2_id] = 1

		if not directed:
			matrix[v2_id][v1_id] = 1

	return matrix


def isAcyclic(m):
	def dfs(matrix, node_id):
		pass

	if len(m) > 1:
		s = 1
		i = 2

		while s < len(m):
			if m[s][i] and m[s][i] == 1:
				i = m[s][]

			elif m[s][i] and m[s][i] == 2:
				pass

			else:
				pass

	else:

		return -1

	return 1


if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--directed", action='store_true', default=False)
	args = p.parse_args()

	with open(args.infile) as f:
		lines = [x.strip() for x in f.readlines()]

	graphs = []
	currentG = []

	for l in lines[2:]:
		if len(l) > 0:
			currentG.append(l)

		else:
			graphs.append(currentG)
			currentG = []

	graphs.append(currentG)

	results = []

	for G in graphs:
		edge_list = [(int(x.split(' ')[0]), int(x.split(' ')[1])) for x in G]
		m = adjacency_matrix(edge_list, directed=True)
		results.append(isAcyclic(m))

	print ' '.join([str(x) for x in results])


