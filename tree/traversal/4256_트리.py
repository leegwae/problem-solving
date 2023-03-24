import sys

input = sys.stdin.readline


def postorder(preorder, inorder):
	if len(preorder) == 0:
		return

	root = preorder[0]
	root_idx = inorder.index(root)
	postorder(preorder[1:root_idx+1], inorder[:root_idx])
	postorder(preorder[root_idx+1:], inorder[root_idx+1:])
	print(root, end=' ')


if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		n = int(input())
		preorder = list(map(int, input().split()))
		inorder = list(map(int, input().split()))
		postorder(preorder, inorder)
		print()
