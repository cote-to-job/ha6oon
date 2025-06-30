
import sys
n, target = map(int, sys.stdin.readline().split())
money = []
for _ in range(n):
    money.append(int(sys.stdin.readline().strip()))
money.sort(reverse=True)
count = 0
for m in money:
    if target == 0:
        break

    count += target //m # 몫
    target %= m # 나머지
        
print(count)