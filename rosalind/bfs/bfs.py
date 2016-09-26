import argparse
import pprint

from Queue import Queue

def adjacency_matrix(edges, v, directed=False):
	matrix = {}

	for e in edges:
		v1_id, v2_id = e

		v1 = {
			"id": v1_id,
			"visited": False
		}

		v2 = {
			"id": v2_id,
			"visited": False
		}

		if v1_id in matrix.keys():

			matrix[v1_id].append(v2)

		else:
			matrix[v1_id] = [v2]

		if not directed:
			if v2_id in matrix.keys():
				matrix[v2_id].append(v1)

			else:
				matrix[v2_id] = [v1]

		else:
			if v2_id not in matrix.keys():
				matrix[v2_id] = []

	if v > len(matrix.keys()):
		add = [x for x in set(range(1, v+1)) - set(matrix.keys())]
		for a_id in add:
			a = {
				"id": a_id,
				"visited": False
			}
			matrix[a_id] = []

	return matrix


def single_source_shortest_path(adjacency_matrix, s):
	Q = Queue()
	D = [-1 if x > 0 else 0 for x in range(0, len(adjacency_matrix.keys()))]

	for c in adjacency_matrix[s]:
		D[c["id"] - 1] = D[s - 1] + 1
		c["visited"] = True
		Q.put(c)

	while not Q.empty():
		i = Q.get()

		for c in adjacency_matrix[i["id"]]:
			if c["visited"] is False and c["id"] != s:
				D[c["id"]-1] = D[i["id"]-1] + 1
				c["visited"] = True
				Q.put(c)

	return D

if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--vertex")
	p.add_argument("--directed", action='store_true', default=False)
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	edge_list = [(int(x.strip().split(' ')[0]), int(x.strip().split(' ')[1])) for x in lines[1:]]

	total_v, _ = [int(x) for x in lines[0].strip().split(' ')]

	adjacency_matrix = adjacency_matrix(edge_list, total_v, directed=args.directed)

	D = single_source_shortest_path(adjacency_matrix, int(args.vertex))

	print ' '.join([str(x) for x in D])
