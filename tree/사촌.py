import sys
from typing import List, DefaultDict
from collections import defaultdict

input = sys.stdin.readline


def parentOf(child: int) -> int:
	for parent in t:
		if child in t[parent]:
			return parent

	return -1


def adj_tree() -> DefaultDict[int, List]:
	tree = defaultdict(list)
	root = 0
	adj = []
	for i in range(1, len(seq)):
		if i != 1 and seq[i - 1] + 1 != seq[i]:
			tree[seq[root]] = adj
			root += 1
			adj = []
		adj.append(seq[i])

	tree[seq[root]] = adj

	return tree


if __name__ == '__main__':
	while True:
		n, k = map(int, sys.stdin.readline().split())
		if n == 0:
			break

		seq = list(map(int, input().split()))
		if n == 1:
			print(0)
			continue

		t = adj_tree()
		k_parent = parentOf(k)
		k_ancestor = parentOf(k_parent)

		if k_ancestor == -1:
			print(0)
			continue

		answer = 0
		for parent_sibling in t[k_ancestor]:
			if parent_sibling == k_parent:
				continue
			answer += len(t[parent_sibling])
		print(answer)
