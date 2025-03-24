
# 그냥 combinations로 다 구해놓고, 조건 만족하는지 체크해나가기
from itertools import combinations

def solution(n, q, ans):
    count = 0
    all_combinations = combinations(range(1, n+1), 5)

    for comb in all_combinations:
        is_valid = True
        comb_set = set(comb)
        for i in range(len(q)):
            match_count = len(set(q[i]) & comb_set)
            if match_count != ans[i]:
                is_valid = False
                break
        if is_valid:
            count += 1

    return count