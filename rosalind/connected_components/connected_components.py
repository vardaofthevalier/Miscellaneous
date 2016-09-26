import argparse
import pprint


class GraphNode(object):
	def __init__(self, value):
		self.value = value
		self.children = []


def adjacency_list(edges, v, directed=False):
	matrix = {}

	for e in edges:
		v1_id, v2_id = e

		v1 = {
			"visited": False,
			"neighbors": []
		}

		v2 = {
			"visited": False,
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
				matrix[v2_id] = v1
				matrix[v2_id]["neighbors"].append(v1_id)

	if v > len(matrix.keys()):
		add = [x for x in set(range(1, v+1)) - set(matrix.keys())]
		for a_id in add:
			a = {
				"visited": False,
				"neighbors": []
			}
			matrix[a_id] = a

	return matrix

def dfs(matrix, node_id):
	try:
		n = matrix.pop(node_id)
	except KeyError:
		pass

	else:
		# print node_id
		if len(n["neighbors"]) > 0:
			for c in n["neighbors"]:
				matrix = dfs(matrix, c)

	return matrix


def connected_components(m):
	cc = 0
	s = m.keys()[0]

	while True:
		# print "CC {n}".format(n = cc)
		m = dfs(m, s)

		cc += 1

		if len(m.keys()) == 0:
			break
		else:
			s = m.keys()[0]

	return cc


if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	p.add_argument("--directed", action='store_true', default=False)
	args = p.parse_args()

	with open(args.infile) as f:
		lines = f.readlines()

	edge_list = [(int(x.strip().split(' ')[0]), int(x.strip().split(' ')[1])) for x in lines[1:]]
	total_v, _ = [int(x) for x in lines[0].strip().split(' ')]

	m = adjacency_list(edge_list, total_v)

	cc = connected_components(m)

	print cc
