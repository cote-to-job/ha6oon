import sys
input = sys.stdin.readline
bands = input().strip()

'''
() -> 레이져 생성 , 스택에서 pop, 현재 쌓여 있는 쇠막대기 수만큼 조각이 생김
(( -> 막대 하나 생성, 스택에 push
)) -> 쇠막대기의 끝.막대 하나 제거== 그 쇠막대기가 마지막으로 잘려서 생긴 조각 하나만 추가.

'''
stack = []
answer = 0
for i in range(len(bands)):
    if bands[i] == '(':
        stack.append('(') # 쇠막대기 생성
    else: # )
        stack.pop()
        if bands[i-1] == '(': # ()
            answer += len(stack) # 스택의 길이 자체가 현재 쌓인 막대기 수 
        elif bands[i-1] == ')': # ))
            answer += 1 # 쇠막대기의 끝. 그 쇠막대기가 마지막으로 잘려서 생긱 조각 하나만 추가.
print(answer)