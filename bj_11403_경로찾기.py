'''
보고 품.

[해설]
이 코드는 방향 그래프의 인접 행렬이 주어졌을 때,
각 정점 i에서 정점 j로 도달 가능한지 여부를 판별해 출력하는 BFS 기반 풀이입니다.

입력으로 주어지는 city는 정점 간 간선 유무를 담은 인접 행렬이며,
visit은 각 정점 쌍 (i, j)에 대해 i에서 j로 도달 가능한지를 기록합니다.
처음에는 모두 0으로 초기화하고, 탐색 과정에서 경로가 확인되면 1로 갱신합니다.

탐색은 각 정점을 from_first로 설정해 시작하며,
그 정점에서 직접 연결된 to_city를 큐에 담고,
큐가 빌 때까지 이어지는 연결(next_to)을 따라가며 visit 값을 갱신합니다.

이 과정을 통해 간접 경로까지 포함한 전체 도달 가능 경로 행렬을 완성합니다.
'''

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

# deque 버전
def solution_deque():
    visit = [[0]*n for _ in range(n)]
    dq = deque()
    for from_first, m in enumerate(city):
        for to_city, moving in enumerate(m):
            if moving == 1 and visit[from_first][to_city] == 0:
                visit[from_first][to_city] = 1
                dq.append(to_city)
                while dq:
                    to_city = dq.popleft()
                    for next_to, next_move in enumerate(city[to_city]):
                        if next_move == 1 and visit[from_first][next_to] == 0:
                            visit[from_first][next_to] = 1
                            dq.append(next_to)

    for i in visit:
        print(*i)
solution_deque()