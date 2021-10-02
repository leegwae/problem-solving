# n, m = map(int, input().split())
#
# adj = [[0] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     adj[u][v] = 1
#     adj[v][u] = 1
#
# visited = [0] * (n + 1)
# def dfs(cur):
#     visited[cur] = 1
#     for i in range(1, n + 1):
#         if adj[cur][i] == 1 and visited[i] != 1:
#             dfs(i)
#
# answer = 0
# for i in range(1, n + 1):
#     if not visited[i]:
#         dfs(i)
#         answer += 1
#
# print(answer)

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visited = [0] * (n + 1)


def dfs(start_v):
    visited[start_v] = 1

    for w in range(1, n + 1):
        if graph[start_v][w] == 1 and visited[w] == 0:
            dfs(w)


count = 0
for v in range(1, n + 1):
    if visited[v] == 0:
        dfs(v)
        count += 1

print(count)