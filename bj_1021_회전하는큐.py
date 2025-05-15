from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))

deq = deque(range(1, m + 1))
count = 0

for t in target:
    # 현재 t의 위치를 기준으로 왼쪽/오른쪽 판단
    idx = deq.index(t)
    if idx <= len(deq) // 2:
        # 왼쪽으로 회전
        deq.rotate(-idx)
        count += idx
    else:
        # 오른쪽으로 회전
        deq.rotate(len(deq) - idx)
        count += len(deq) - idx
    deq.popleft()

print(count)