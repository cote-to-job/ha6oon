# deque - 선입선출
from collections import deque
def solution(skill, skill_trees):
    s_list = [i for i in skill]
    s_deque = deque(s_list)
    s_set = set(s_list)
    check = s_deque.popleft()
    answer = 0

    for tree in skill_trees:
        s_deque = deque(s_list)       
        flag = True
        for s in tree:
            if s not in s_set:
                continue
            else:
                check = s_deque.popleft()
                if check == s:
                    continue
                else:
                    flag = False
                    break
        if flag:
            answer += 1
    return answer
    