import sys

input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(1, N + 1):
	root, left, right = input().split()
	tree[root] = [left, right]


def preorder(node):
	if node == '.' or node not in tree:
		return

	print(node, end='')
	left, right = tree[node]
	preorder(left)
	preorder(right)


def inorder(node):
	if node == '.' or node not in tree:
		return

	left, right = tree[node]
	inorder(left)
	print(node, end='')
	inorder(right)


def postorder(node):
	if node == '.' or node not in tree:
		return

	left, right = tree[node]
	postorder(left)
	postorder(right)
	print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')