from itertools import combinations, product
from collections import Counter
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    indices = list(range(n))
    max_win = -1
    best_comb = []

    for a_indices in combinations(indices, n // 2):
        b_indices = [i for i in indices if i not in a_indices]
        a_dice = [dice[i] for i in a_indices]
        b_dice = [dice[i] for i in b_indices]

        a_sums = [sum(p) for p in product(*a_dice)]
        b_sums = [sum(p) for p in product(*b_dice)]

        b_sums.sort()
        win = 0

        for a in a_sums:
            # B에서 a보다 작은 값 개수
            win += bisect_left(b_sums, a)

        if win > max_win:
            max_win = win
            best_comb = a_indices

    return sorted([i + 1 for i in best_comb])



'''
테스트 케이스 3개는 맞았는데, 최종제출 시간초과로 제출안됨. (18까지 통과, 19~26 실패)

from itertools import combinations, product

def solution(dice):
    n = len(dice)
    n_list = list(range(n))  
    max_win = -1
    best_pick = []

    for a_pick in combinations(n_list, n // 2):
        b_pick = [i for i in n_list if i not in a_pick]

        a_dice = [dice[i] for i in a_pick]
        b_dice = [dice[i] for i in b_pick]

        a_sums = [sum(x) for x in product(*a_dice)]
        b_sums = [sum(x) for x in product(*b_dice)]

        win = 0
        for a in a_sums:
            for b in b_sums:
                if a > b:
                    win += 1

        if win > max_win:
            max_win = win
            best_pick = a_pick

    return sorted([i + 1 for i in best_pick])
'''