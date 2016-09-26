import argparse
import pprint

from Queue import Queue


def adjacency_matrix(edges, directed=False):
	matrix = {}

	for e in edges:
		v1_id, v2_id = e

		v1 = {
			"color": None,
			"neighbors": []
		}

		v2 = {
			"color": None,
			"neighbors": []
		}

		if v1_id in matrix.keys():
			matrix[v1_id]["neighbors"].append(v2_id)

		else:
			matrix[v1_id] = v1
			matrix[v1_id]["neighbors"].append(v2_id)

		if not directed:
			if v2_id in matrix.keys():
				matrix[v2_id]["neighbors"].append(v1_id)

			else:
				matrix[v2_id] = v2
				matrix[v2_id]["neighbors"].append(v1_id)

	return matrix


def isBipartite(m):
	s = m.keys()[0]
	m[s]["color"] = 0  # red, but we'll use 0 and 1 for red and blue instead

	Q = Queue()

	for n in m[s]["neighbors"]:
		n = m[n]

		if n["color"] is None:
			n["color"] = int(not m[s]["color"])

		elif n["color"] != m[s]["color"]:
			continue

		else:
			return -1

		Q.put(n)

	while not Q.empty():
		i = Q.get()

		for n in i["neighbors"]:
			n = m[n]
			if n["color"] is None:
				n["color"] = int(not i["color"])

			elif n["color"] != i["color"]:
				continue

			elif n["color"] == i["color"]:
				return -1

			Q.put(n)

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
		edge_list = [(int(x.split(' ')[0]), int(x.split(' ')[1])) for x in G[1:]]

		m = adjacency_matrix(edge_list)

		results.append(isBipartite(m))

	print ' '.join([str(x) for x in results])
