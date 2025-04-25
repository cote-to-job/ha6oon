# 그리디, 스택
def solution(number, k):
    stack = []
    for num in number:
        # 현재 숫자보다 stack 마지막 숫자가 작으면 pop
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 다 돌고 나서 k가 남아있으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
