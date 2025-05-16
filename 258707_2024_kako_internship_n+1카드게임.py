"""
[카드 게임 라운드 최대화 알고리즘 설명]

이 문제는 매 라운드마다 카드 두 장을 사용해 특정 합(n + 1)을 만들 수 있는지 판단하고,
최대 몇 라운드까지 진행할 수 있는지를 구하는 시뮬레이션 문제입니다.

게임 진행 로직은 다음과 같습니다:

1. 처음 n/3장의 카드를 손패(my_cards)로 받습니다.
2. 이후 매 라운드마다 카드 2장을 뽑아 킵 카드(keep_cards)에 저장합니다.
3. 각 라운드에서 사용할 수 있는 카드 조합은 아래의 우선순위로 판단합니다:
   - (1) 손패에서 두 장을 골라 타겟 합을 만들 수 있다면 동전 소모 없이 라운드 진행
   - (2) 손패 1장 + 킵 카드 1장 조합으로 만들 수 있다면 동전 1개 소모 후 라운드 진행
   - (3) 킵 카드 2장 조합으로 만들 수 있다면 동전 2개 소모 후 라운드 진행
4. 위 세 경우 중 하나도 성립하지 않으면 게임 종료
5. 최초 손패만으로 1라운드를 진행할 수 있는 경우가 있으므로,
   최종 결과에 1을 더해 반환합니다 (보정용 +1)

이 알고리즘은 모든 카드 조합을 탐색하면서도 매 라운드에 하나의 조합만 채택하므로,
복잡도는 라운드 수(최대 n/2)에 비례하여 효율적으로 동작합니다.

참고문헌 : https://iosun.tistory.com/44
"""

from itertools import combinations

def solution(coin, cards):
    n = len(cards)
    target = n + 1
    my_cards = set(cards[:n // 3])
    keep_cards = []
    round_count = 1
    draw_index = n // 3

    while draw_index + 1 < n:
        # 카드 2장 뽑아서 킵
        keep_cards.append(cards[draw_index])
        keep_cards.append(cards[draw_index + 1])
        draw_index += 2

        # case 1: my_cards에서 합이 target인 조합 찾기 (코인 0개)
        found = False
        for a, b in combinations(my_cards, 2):
            if a + b == target:
                my_cards.remove(a)
                my_cards.remove(b)
                round_count += 1
                found = True
                break
        if found:
            continue

        # case 2: my_cards + keep_cards 조합 (코인 1개)
        if coin >= 1:
            for a in my_cards:
                for b in keep_cards:
                    if a + b == target:
                        my_cards.remove(a)
                        keep_cards.remove(b)
                        coin -= 1
                        round_count += 1
                        found = True
                        break
                if found:
                    break
        if found:
            continue

        # case 3: keep_cards에서 합이 target인 조합 (코인 2개)
        if coin >= 2:
            for a, b in combinations(keep_cards, 2):
                if a + b == target:
                    keep_cards.remove(a)
                    keep_cards.remove(b)
                    coin -= 2
                    round_count += 1
                    found = True
                    break
        if found:
            continue

        # 아무 경우에도 해당하지 않으면 종료
        break

    return round_count



'''
실패코드
from itertools import combinations
from collections import deque

def solution(coin, cards):
    n = len(cards)
    target = n + 1
    initial = set(cards[:n//3])
    deck = deque(cards[n//3:])
    round_num = 1

    def has_valid_pair(hand):
        hand_list = list(hand)
        for i in range(len(hand_list)):
            for j in range(i+1, len(hand_list)):
                if hand_list[i] + hand_list[j] == target:
                    return (hand_list[i], hand_list[j])
        return None

    def dfs(index, coins, hand):
        nonlocal round_num, max_round
        if index >= len(deck):
            max_round = max(max_round, round_num)
            return

        if len(deck) - index < 2:
            max_round = max(max_round, round_num)
            return

        # 다음 라운드 카드 뽑기
        card1, card2 = deck[index], deck[index + 1]
        candidates = []

        # 경우의 수: 둘 다 안 가지기
        candidates.append((coins, set(hand), 0))

        # 경우의 수: 하나만 가지기
        if coins >= 1:
            candidates.append((coins - 1, set(hand) | {card1}, 1))
            candidates.append((coins - 1, set(hand) | {card2}, 1))

        # 경우의 수: 둘 다 가지기
        if coins >= 2:
            candidates.append((coins - 2, set(hand) | {card1, card2}, 2))

        for new_coins, new_hand, used in candidates:
            pair = has_valid_pair(new_hand)
            if pair:
                # 다음 라운드로 진입할 수 있음
                new_hand.remove(pair[0])
                new_hand.remove(pair[1])
                round_num += 1
                dfs(index + 2, new_coins, new_hand)
                round_num -= 1
            else:
                # 진입 불가 → 최대 라운드 기록
                max_round = max(max_round, round_num)

    max_round = 0
    dfs(0, coin, initial)
    return max_round 
'''