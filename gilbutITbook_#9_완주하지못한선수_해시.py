from collections import Counter
def solution(participant, completion):
    answer = ''
    part = Counter(participant)
    comp = Counter(completion)
    answer = ''.join(list(part - comp))
    return answer
