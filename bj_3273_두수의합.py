import sys

n = int(sys.readline().strip())
n_list = list(map(int, sys.readline().split()))
target = int(sys.readline().strip())


n_list.sort()
start, end = 0, n-1
answer = 0

while start <= end:
    current_sum = n_list[start] + n_list[end]
    if current_sum == target:
        answer += 1
        start += 1
        end -= 1
    elif current_sum < target:
        start += 1
    else:
        end -= 1
print(answer)