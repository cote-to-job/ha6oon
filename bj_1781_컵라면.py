
'''
[생각]
단순 정렬 + 그리디로 풀려고 해도, "어떤 문제를 버릴지"를 빠르게 결정해야 하는데, 
이걸 O(1)에 하는 방법이 없음.
(N^2)으로 할 수는 있지만, N이 최대 200,000이라 시간 초과.

매번 '시간 내에 풀 수 있는 문제'를 골라야 하고, 가장 가치 없는 문제를 빠르게 버려야함.
이걸 효율적으로 처리하는 자료구조는 우선순위 큐.

[로직]
1. 데드라인 순으로 정렬해.
2. 하나씩 문제를 보면서, 일단 풀어.
3. 시간이 초과하면 '지금까지 푼 문제 중에서 제일 컵라면 적은 문제'를 버려.
4. 마지막에 남은 문제들의 컵라면 수를 다 더해.

*heap : 그냥 일단 다 넣어보고, 시간 초과 상황에서 제일 컵라면 적은 문제를 버림. 결과적으로 최대 컵라면 수를 유지할 수 있음

'''
import sys
import heapq

input = sys.stdin.readline
n = int(input())
problems = []

for _ in range(n):
    deadline, ramen = map(int, input().split())
    problems.append((deadline, ramen))

problems.sort()  # 데드라인 순서대로 정렬

heap = []  # 지금까지 푼 문제들의 컵라면 수를 저장할 힙

for deadline, ramen in problems:
    heapq.heappush(heap, ramen)  # 일단 문제를 푼다고 생각하고 넣어
    if len(heap) > deadline:  # 시간이 초과하면
        heapq.heappop(heap)  # 가장 컵라면이 적은 문제를 버려

print(sum(heap))  # 남은 문제들의 컵라면 합
