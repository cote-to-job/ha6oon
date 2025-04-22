def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) -1
    # 맨앞과 맨 뒤 비교해서 탈 수 있는지 확인
    while end - start > 0 :
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    if end == start: # 무게는 추과하지 않지만 한 명만 남는 경우
        answer += 1
        
    return answer