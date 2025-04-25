def solution(diffs, times, limit):
    # 특정 숙련도(level)로 퍼즐을 제한 시간 안에 풀 수 있는지 판단하는 함수
    def is_ok(level):
        total = times[0]  # 첫 퍼즐은 무조건 맞출 수 있음 (난이도는 항상 1로 고정)
        for i in range(1, len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1]

            if diff <= level:
                # 숙련도가 난이도보다 크거나 같으면 정답 처리
                total += time_cur
            else:
                # 틀린 횟수: 숙련도보다 난이도가 얼마나 큰지
                wrong = diff - level
                # 틀릴 때마다 걸리는 시간: (이전 시간 + 현재 시간) * 틀린 횟수 + 마지막에 맞히는 시간
                total += wrong * (time_cur + time_prev) + time_cur

            # 제한 시간 초과 시 False 반환
            if total > limit:
                return False
        return True

    # 이분 탐색으로 최소 숙련도(level) 탐색
    # 최적의 숙련도는 1~ max(diffs) 사이의 값일 테니, 그 사이를 이분탐색으로 최적의 값 찾아감.
    left, right = 1, max(diffs)
    answer = right  # 최악의 경우로 초기화

    while left <= right:
        mid = (left + right) // 2
        if is_ok(mid):
            answer = mid  # 현재 숙련도로 클리어 가능 → 더 낮은 숙련도 가능한지 확인
            right = mid - 1
        else:
            left = mid + 1  # 현재 숙련도로는 불가능 → 더 높은 숙련도로 시도

    return answer
