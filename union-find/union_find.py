import sys

input = sys.stdin.readline


# # 2. 찾기
# def find(u):
# 	if parent[u] == u:
# 		return u
#
# 	return find(parent[u])

# 2. 최적화된 찾기
def find(u):
	if parent[u] == u:
		return u

	parent[u] = find(u)
	return parent[u]

# # 3. 합치기
# def union(u, v):
# 	u, v = find(u), find(v)
#
# 	if u == v:
# 		return
#
# 	parent[u] = v


# 3. 최적화된 합치기
def union(u, v):
	u, v = find(u), find(v)

	if u == v:
		return

	if rank[u] > rank[v]:
		u, v = v, u
	parent[u] = v
	if rank[u] == rank[v]:
		rank[v] += 1

if __name__ == '__main__':
	N = int(input())
	# 1. 초기화
	parent = [i for i in range(N)]

	# 트리의 레벨을 저장한다.
	rank = [0] * N
