import sys
n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().split()))

count = 0

for number in n_list:
    flag = True
    if number == 1:
        continue
    for i in range(2, number//2+1):
        if number % i == 0:
            flag = False
            break
    if flag:
        count += 1
print(count)