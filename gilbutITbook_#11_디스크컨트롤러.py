import heapq

def solution(jobs):
    # 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높습니다.
    jobs.sort()   # (요청 시각, 소요 시간) 순으로 정렬

    n = len(jobs)
    now = 0
    count = 0
    idx = 0
    answer = 0
    hq =[] # 미리 해놔야하는거 잊지말기
    while count < n:
        while idx < n and now >= jobs[idx][0]:
            heapq.heappush(hq, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if hq:
            time, i = heapq.heappop(hq)
            now += time
            count += 1
            answer += now - i
        else:
            now = jobs[idx][0]
    return answer//n