import math
import argparse

def binary_search(A, k, i=None):
	if len(A) == 0:
		return -1
		
	med_i = len(A)/2
	med = A[med_i]
	
	if i is None:
		i = med_i
		
	if k == med:
		return i + 1
	
	elif k > med:
		r = A[med_i+1:]
		return binary_search(r, k, i=i+len(r)-(len(r) - 1)/2)
	
	else:
		l = A[0:med_i]
		return binary_search(l, k, i=i-len(l)+len(l)/2)
	
if __name__ == "__main__":
	p = argparse.ArgumentParser()
	p.add_argument("infile")
	args = p.parse_args()
	
	with open(args.infile) as f:
		lines = f.readlines()
		
	array = [int(a) for a in lines[2].strip().split(' ')]
	search = [int(k) for k in lines[3].strip().split(' ')]
	results = []
	
	for s in search:
		results.append(str(binary_search(array, s)))
		
	print ' '.join(results)