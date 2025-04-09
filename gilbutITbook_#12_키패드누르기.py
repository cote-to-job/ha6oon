def solution(numbers, hand):
    answer = ''
    # 번호처럼 쓰기: * = 10, 0 = 11, # = 12
    left_pos = 10  # *
    right_pos = 12  # #

    for num in numbers:
        if num == 0:
            num = 11
        
        if num % 3 == 1:  # 왼쪽 열
            answer += 'L'
            left_pos = num
        elif num % 3 == 0:  # 오른쪽 열
            answer += 'R'
            right_pos = num
        else:  # 가운데 열
            # 거리 계산
            def dist(a, b):
                return abs((a - 1)//3 - (b - 1)//3) + abs((a - 1)%3 - (b - 1)%3)

            l_dist = dist(left_pos, num)
            r_dist = dist(right_pos, num)

            if l_dist < r_dist:
                answer += 'L'
                left_pos = num
            elif r_dist < l_dist:
                answer += 'R'
                right_pos = num
            else:  # 같으면 hand 기준
                if hand == "right":
                    answer += 'R'
                    right_pos = num
                else:
                    answer += 'L'
                    left_pos = num

    return answer
