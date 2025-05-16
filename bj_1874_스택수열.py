l = int(input())
stack = []
before_num = 1
answer = []
flag = True
for i in range(l):
    num = int(input())
    while before_num <= num:
        stack.append(before_num)
        answer.append('+')
        before_num += 1
        
        
    if stack[-1] == num :
        stack.pop()
        answer.append('-')
    else:
        flag = False
        break
if flag:
    for i in answer:
        print(i)
else:
    print('NO')