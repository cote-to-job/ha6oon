from collections import deque
import sys
queue = deque([])
n = int(sys.stdin.readline().strip())
for _ in range(n):
    cmd_list = list(map(str, sys.stdin.readline().split()))
    if len(cmd_list) == 2: #if cmd_list[0] == 'push':
        queue.append(cmd_list[1])
    else:
        if cmd_list[0] == 'front':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue[0])
        elif cmd_list[0] == 'back':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue[-1])
        elif cmd_list[0] == 'size':
            print(len(queue))
        elif cmd_list[0] == 'empty':
            if len(queue) == 0:
                print('1')
            else:
                print('0')
        else: # cmd_list[0] == 'pop':
            if len(queue) == 0:
                print('-1')
            else:
                q = queue.popleft()
                print(q)