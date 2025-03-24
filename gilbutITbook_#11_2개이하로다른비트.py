def solution(numbers):
    """
    ✅ 문제 풀이 전략
    - f(x): x보다 크면서 비트가 1~2개 다른 수 중 가장 작은 수
    - 비트가 다른 개수: XOR 연산을 통해 확인 가능
    - x가 짝수라면:
        - 끝 비트가 0 → x + 1 하면 1비트만 달라짐 → f(x) = x + 1
    - x가 홀수라면:
        - 끝이 1로 끝나므로 x + 1은 여러 비트가 바뀜
        - 해결법:
            - x ^ (x + 1) → 바뀐 비트 위치 찾기
            - 이를 통해 바뀐 뒤쪽 비트(2번째 이후)를 보정
            - f(x) = x + 1 + ((x ^ (x + 1)) >> 2)
    """

    answer = []
    for x in numbers:
        if x % 2 == 0:
            # 짝수인 경우: x + 1이 비트 1개만 다르므로 바로 반환
            answer.append(x + 1)
        else:
            # 홀수인 경우:
            # x ^ (x+1): x와 x+1의 다른 비트 위치를 구함
            # >> 2: 가장 작은 2개 비트 외의 영향을 없앰 (2번째 자리 이후만 마스크)
            bit = (x ^ (x + 1)) >> 2

            # x + 1로 한 번 오른쪽 비트를 바꾸고,
            # bit를 더해 바뀐 이후 비트를 보정하여 f(x) 계산
            next_val = x + 1 + bit
            answer.append(next_val)
    
    return answer
