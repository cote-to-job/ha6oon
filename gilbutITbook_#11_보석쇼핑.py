'''
모든 종류의 보석을 최소 한번 포함하는 가장 짧은 구간 찾기 -> 투 포인터 + 해시맵
1. 투 포인터(start, end)를 이용해 슬라이딩 윈도우 방식으로 gems 리스트를 탐색함. 
2. 윈도우에 보석을 하나씩 추가하면서 종류가 n개가 되면, start를 이동시키며 최소 구간을 찾음
    윈도우: [start ---- end]
    1. 보석 종류가 다 찼다 → start를 당겨서 최소화 시도
    2. start 위치 보석 개수 -= 1
    3. 만약 0개 → 종류 하나 빠짐 → 종류 부족해짐 → 다시 end 확장
    
    핵심 포인트
    start를 당길 때 구간이 더 짧아질 수 있어서 시도해보는 거고,
    조건이 만족된 순간에만 answer를 갱신하니까
    이후 조건이 무너져도 이미 좋은 결과를 기록해놨기 때문에 걱정 X
'''
from collections import defaultdict
def solution(gems):
    kind = len(set(gems)) # 전체 보석 종류 수
    gem_dict = defaultdict(int)  # 현재 윈도우(구간) 안의 보석 개수
    answer = [0, len(gems) -1]
    start, end = 0, 0
    gem_dict[gems[0]] = 1
    
    while start < len(gems) and end < len(gems):
        if len(gem_dict) < kind:
            end  += 1
            if end == len(gems):
                break
            gem_dict[gems[end]] += 1
        else:
            if (end - start) < answer[1] - answer[0] :
                answer = [start, end]
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
    return [answer[0] + 1, answer[1] + 1]

'''
# 정확성 테스트 통과, 효율성 테스트 통과 X
def solution(gems):
    answer = []
    standard = set(gems)
    n = len(standard)
    answer = [0, len(gems)-1]
    
    for i in range(0, len(gems)):
        buy_set = set()
        for j in range(i,len(gems)):
            buy_set.add(gems[j])
            if len(buy_set) == n:
                if (j - i) < (answer[1] - answer[0]):
                    answer= [i, j]
                break
            
            
    return [answer[0] +1, answer[1] + 1]
'''
