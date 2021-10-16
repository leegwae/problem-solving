from typing import List
from collections import defaultdict, deque

class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     # 각 정점들의 진입 차수를 저장한다.
    #     indegree = [0] * numCourses
    #     # 과목 간의 선수, 후수 관계를 나타낸 그래프
    #     graph = defaultdict(list)
    #
    #     # 인접 리스트로 그래프를 표현하고
    #     # 각 정점들의 진입 차수를 게산한다.
    #     for v, w in prerequisites:
    #         graph[v].append(w)
    #         indegree[w] += 1
    #
    #     # 진입 차수가 0인 정점들을 큐에 넣는다.
    #     q: deque = deque([])
    #     for v in range(numCourses):
    #         if indegree[v] == 0:
    #             q.append(v)
    #
    #     # 각 정점을 위상 정렬로 돌면서 사이클이 있는지 확인한다.
    #     for _ in range(numCourses):
    #         if not q:
    #             return False
    #
    #         v = q.popleft()
    #         for w in graph[v]:
    #             indegree[w] -= 1
    #             if indegree[w] == 0:
    #                 q.append(w)
    #
    #     return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        visited = [0] * numCourses
        finished = [0] * numCourses

        def dfs(curr):
            # 해당 정점을 이용한 모든 노드의 탐색이 끝난 경우(순환 구조가 있는 경우)
            if finished[curr]:
                return False

            # 이미 방문한 정점인 경우
            if visited[curr]:
                return True  # 이미 방문한 정점인 경우

            # 정점을 방문하였음
            visited[curr] = 1
            for nxt in adj[curr]:
                if dfs(nxt):  # 이미 방문한 정점인 경우 False를 반환
                    return True
            finished[curr] = 1  # 자손 정점의 방문이 전부 끝났음
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    print(s.canFinish(numCourses, prerequisites))