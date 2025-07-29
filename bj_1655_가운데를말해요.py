/******************************************************************************
[풀이 알고리즘즘]
두 개의 힙을 사용해 입력되는 숫자들의 중간값을 매번 빠르게 구하는 방법
- left: 최대 힙 (중간값 이하의 값들을 저장, 파이썬은 최소 힙만 지원하므로 음수로 변형)
- right: 최소 힙 (중간값 이상의 값들을 저장)
두 힙의 크기를 균형 있게 유지하며, 항상 left의 루트가 전체 중간값이 됨

[힙 두개 사용 이유]
- 매번 '중간값'을 실시간으로 빠르게 구해야 해
- 입력이 최대 100,000개라서 매번 정렬하면 시간 초과
- 그래서 두 개의 힙을 사용해서 중간값을 O(log N)에 유지하는 게 최적

*******************************************************************************/
import heapq
import sys

input = sys.stdin.readline

n = int(input())
left = []  # 최대 힙 (음수로 넣음)
right = []  # 최소 힙

for _ in range(n):
    num = int(input())

    # 최대 힙에 먼저 넣음
    heapq.heappush(left, -num)

    # left의 최대값 > right의 최소값이면 교환
    if right and -left[0] > right[0]:
        max_left = -heapq.heappop(left)
        heapq.heappush(right, max_left)

    # 두 힙의 크기 균형 맞추기
    if len(left) > len(right) + 1:
        max_left = -heapq.heappop(left)
        heapq.heappush(right, max_left)
    elif len(right) > len(left):
        min_right = heapq.heappop(right)
        heapq.heappush(left, -min_right)

    # 중간값 출력 (작은 쪽 중간값, 즉 left의 루트)
    print(-left[0])
