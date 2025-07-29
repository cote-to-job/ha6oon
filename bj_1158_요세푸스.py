import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ppl = [i for i in range(1, n + 1)]
result = []

idx = 0
while ppl:
    idx = (idx + k - 1) % len(ppl)
    result.append(ppl.pop(idx))

print(f"<{', '.join(map(str, result))}>")

'''
# deque를 활용한 요세푸스 문제 풀이
from collections import deque

n, k = map(int, input().split())

dq = deque(range(1, n + 1))  # [1, 2, ..., n]
result = []

while dq:
    dq.rotate(-(k - 1))  # 왼쪽으로 k-1번 회전 → k번째가 맨 앞으로 오도록
    result.append(dq.popleft())  # 맨 앞 제거

print(f"<{', '.join(map(str, result))}>")
'''