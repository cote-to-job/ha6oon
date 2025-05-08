# 시뮬레이션
'''
다시풀어보기..
풀이 요약
1. 포인트 번호를 좌표로 매핑하고, 각 로봇의 전체 이동 경로를 초 단위로 시뮬레이션합니다.
2. 이동할 때 r좌표를 먼저 이동하고, 이후 c좌표를 이동하는 규칙을 따릅니다.
3. 매 초마다 로봇들의 위치를 체크하여, 같은 좌표에 2대 이상 모이면 위험 상황으로 카운트합니다.
4. 모든 로봇이 이동을 마칠 때까지 반복하고, 총 위험 상황 발생 횟수를 반환합니다.

'''

from collections import defaultdict

def solution(points, routes):
    # 1. 포인트 번호 -> (r, c) 매핑
    point_map = {i+1: (r, c) for i, (r, c) in enumerate(points)}
    
    # 2. 각 로봇의 이동 경로를 시간 단위로 미리 계산
    robots_paths = []  # robots_paths[i][t] = 로봇 i가 t초에 있는 위치
    
    for route in routes:
        path = []  # 한 로봇의 이동 경로
        # 출발 포인트
        cr, cc = point_map[route[0]]
        path.append((cr, cc))
        
        # 순서대로 이동
        for point_num in route[1:]:
            nr, nc = point_map[point_num]
            
            # r좌표 먼저 맞추기
            while cr != nr:
                if cr < nr:
                    cr += 1
                else:
                    cr -= 1
                path.append((cr, cc))
                
            # c좌표 맞추기
            while cc != nc:
                if cc < nc:
                    cc += 1
                else:
                    cc -= 1
                path.append((cr, cc))
        
        robots_paths.append(path)
    
    # 3. 시뮬레이션: 초마다 로봇들의 위치를 확인
    time = 0
    risk_count = 0
    finished = [False] * len(robots_paths)  # 각 로봇이 경로를 다 끝냈는지 체크
    
    while not all(finished):
        loc_counter = defaultdict(int)
        
        for idx, path in enumerate(robots_paths):
            if time < len(path):
                loc = path[time]
                loc_counter[loc] += 1
            else:
                finished[idx] = True  # 이 로봇은 다 끝남
        
        # 위험 상황: 2대 이상이 같은 위치에 있을 때
        for loc, cnt in loc_counter.items():
            if cnt >= 2:
                risk_count += 1
        
        time += 1  # 다음 초로
        
    return risk_count
