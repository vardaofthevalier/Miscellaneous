import argparse


def insertion_sort_swaps(A):
    swap_count = 0
    for i in range(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k-1]:
            ak = A[k]
            A[k] = A[k-1]
            A[k-1] = ak

            swap_count += 1
            k -= 1

    return swap_count

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("infile")
    args = p.parse_args()

    with open(args.infile) as f:
        lines = f.readlines()

    array = [int(x) for x in lines[1].strip().split(' ')]
    swaps = insertion_sort_swaps(array)

    print swaps