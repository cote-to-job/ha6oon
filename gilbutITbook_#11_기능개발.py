def solution(progresses, speeds):
    

    def end_time(progress, speed):
        day = 0
        while(progress < 100):
            progress += speed
            day += 1
        return day
    
    days = []
    n = len(progresses)
    
    # 일 끝나는데 걸리는 날짜 구함
    for idx in range(n):
        day = end_time(progresses[idx],speeds[idx])
        days.append(day)
    print(days)
    
    # 큐 활용
    answer = []
    while days:
        a = days.pop(0)
        cnt = 1
        for d in days:
            if a >= d:
                print(a, d)
                cnt += 1
            else:
                break
            
        for _ in range(cnt-1):
            days.pop(0)
        answer.append(cnt)

    return answer