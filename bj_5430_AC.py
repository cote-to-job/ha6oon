from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_input = input().strip()

    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_input[1:-1].split(',')))

    reverse_flag = False
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            reverse_flag = not reverse_flag
        elif cmd == 'D':
            if not arr:
                error_flag = True
                break
            if reverse_flag:
                arr.pop()
            else:
                arr.popleft()

    if error_flag:
        print("error")
    else:
        if reverse_flag:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")
