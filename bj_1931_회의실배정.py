import sys
n = int(sys.stdin.readline().strip())
schedule = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    schedule.append((start, end))

schedule.sort(key=lambda x:(x[1], x[0])) # 끝시점을 기준으로 정렬
end = schedule[0][1]
count = 1
for i in range(1,n):
    if schedule[i][0] >= end:
        end = schedule[i][1]
        count += 1
print(count)