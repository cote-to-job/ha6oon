import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    pw = input().rstrip()
    left = []   # 커서 왼쪽
    right = []  # 커서 오른쪽

    for ch in pw:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)

    print(''.join(left + right[::-1]))
