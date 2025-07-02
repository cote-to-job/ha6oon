'''
- 메모리 초과 방지를 위해 hq 길이를 n만큼 유지하는 방법
1. 첫번재 입력값을 hq에 최소힙구조로 넣기
2.  그 다음 입력값부터 hq의 최솟값보다 큰 수가 들어오면 hq 원소를 교체해주기
-> 결국 hq엔 가장 큰 n개의 수만 남고, 최소힙이기 때문에 pop()해줌.

'''

import sys, heapq

input = sys.stdin.readline
n = int(input())
hq = []
for i in range(n):
	num_list = list(map(int, input().split()))
	if not hq:
		for num in num_list:
			heapq.heappush(hq, num) 
	else:
		for num in num_list: 
			if hq[0] < num: 
				heapq.heappush(hq, num) 
				heapq.heappop(hq) 
print(hq[0])