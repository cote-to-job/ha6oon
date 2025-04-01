# 수학적인 순열의 규칙을 이용해서, 전체 순열을 직접 만들지 않고도 k번째 순열을 빠르게 구하는 방법
import math
def solution(n, k):
    numbers = list(range(1, n + 1))  # 줄을 설 사람들 [1, 2, ..., n]
    result = []

    k -= 1  # 0-index 조정

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)  # (i-1)! 계산
        idx = k // fact  # 현재 자리 숫자의 인덱스
        result.append(numbers.pop(idx))  # 숫자 선택 및 제거
        k %= fact  # 다음 순서를 위해 k 갱신

    return result

'''
# 효율성 테스트 실패 코드
from itertools import permutations
def solution(n, k): 
    how_list = list(permutations([i+1 for i in range(n)], n))
    answer = how_list[k-1]
    return answer
'''