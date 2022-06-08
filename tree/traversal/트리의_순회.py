import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def print_preorder(in_left, in_right, post_left, post_right):
	global inorder, postorder
	if post_right - post_left == 0:
		return

	root = postorder[post_right - 1]
	root_idx = position[root]
	subtree_len = root_idx - in_left

	print(root, end=' ')

	print_preorder(in_left, root_idx, post_left, post_left + subtree_len)
	print_preorder(root_idx + 1, in_right, post_left + subtree_len, post_right - 1)


# def print_preorder(inorder, postorder):
# 	if len(postorder) == 0:
# 		return
#
# 	root = postorder[-1]
# 	root_idx = inorder.index(root)
# 	inorder_L = inorder[:root_idx]
# 	inorder_R = inorder[root_idx + 1:]
# 	subtree_len = len(inorder_L)
# 	postorder_L = postorder[:subtree_len]
# 	postorder_R = postorder[subtree_len:-1]
#
# 	print(root, end=' ')
# 	print_preorder(inorder_L, postorder_L)
# 	print_preorder(inorder_R, postorder_R)
#
# print_preorder(inorder, postorder)

if __name__ == '__main__':
	N = int(input())
	inorder = list(map(int, input().split()))
	postorder = list(map(int, input().split()))
	position = [-1] * (N + 1)
	for idx, root in enumerate(inorder):
		position[root] = idx
	print_preorder(0, N, 0, N)
