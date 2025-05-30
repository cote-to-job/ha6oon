import sys
# 큐 -> deque로 구현
from collections import deque

def bridge_crossing_time(n, w, L, truck_weights):
    bridge = deque([0] * w)  # 초기 다리 상태 (w만큼 0)
    time = 0
    total_weight = 0
    trucks = deque(truck_weights)

    while trucks or total_weight > 0:
        time += 1
        # 트럭 하나 내보내기
        exited = bridge.popleft()
        total_weight -= exited

        # 다음 트럭이 들어갈 수 있는지 확인
        if trucks and total_weight + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)  # 빈 공간 추가

    return time

n, w, L = map(int, sys.stdin.readline().split())
truck_weights = list(map(int, sys.stdin.readline().split()))
print(bridge_crossing_time(n, w, L, truck_weights)) 