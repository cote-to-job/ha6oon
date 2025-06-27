# heapq 자료구조 2개 사용 -> 최소힙, 최대힙으로 구성
# heapq.pop()은 deque 자료구조처럼 양쪽에서 뺴는 연산은 불가능. 항상 인덱스 0 (루트)만 제거 가능. -> visited 사용해서 뺀거 표시

import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k  # 삽입마다 고유 인덱스 부여
    idx = 0  # 고유 인덱스

    for _ in range(k):
        command, num = input().split()
        num = int(num)

        if command == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
            idx += 1

        elif command == "D":
            if num == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:  # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # visited 정보 활용해서 delete(D)한거 힙별로 삭제해주기
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
