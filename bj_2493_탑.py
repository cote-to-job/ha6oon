n = int(input())
heights = list(map(int, input().split()))
result = [0] * n
stack = []

for i in range(n):
    # 현재 탑보다 낮은 탑은 의미 없으니 제거
    while stack and stack[-1][1] < heights[i]:
        stack.pop()
    
    # 스택에 남아 있는 것이 있다면, 수신 가능한 탑
    if stack:
        result[i] = stack[-1][0] + 1  # 인덱스를 번호로 바꿔서 저장
    
    # 현재 탑을 스택에 추가
    stack.append((i, heights[i]))

print(' '.join(map(str, result)))
