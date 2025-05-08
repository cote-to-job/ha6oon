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
