from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visited = set()
    queue = deque([(begin, 0)]) # 단어, 횟수
    
    while queue:
        current_word, count = queue.popleft()
        if current_word == target :
            return count
        for word in words:
            if word not in visited and can_convert(current_word, word):
                visited.add(word)
                queue.append((word, count + 1))
    
# 한 글자만 다른지 확인하는 함수
def can_convert(w1, w2):
    diff = 0
    for a, b in zip(w1, w2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

            
            