from collections import defaultdict
import bisect

'''
해결책: 이진 탐색 + 정렬 기반 방식
원래 쓰던 딕셔너리 + startswith / endswith 방식에 정렬 + 이진 탐색 (bisect)을 활용

*프로세스
1. 길이별로 단어를 분류 + 정렬
2. 쿼리가 접두사 패턴이면 → bisect_left/right로 접두사 범위 검색
3. 쿼리가 접미사 패턴이면 → 단어를 뒤집어서 정렬한 후, 쿼리도 뒤집어 같은 방식으로 처리

'''

def solution(words, queries):
    # 길이별 단어 목록 (정방향)
    word_dict = defaultdict(list)
    # 길이별 단어 목록 (역방향: 접두사 와일드카드 대비)
    reversed_dict = defaultdict(list)

    for word in words:
        word_dict[len(word)].append(word)
        reversed_dict[len(word)].append(word[::-1])

    # 정렬
    for length in word_dict:
        word_dict[length].sort()
        reversed_dict[length].sort()

    result = []
    for q in queries:
        length = len(q)

        if q[0] != '?':  # 접미사에 와일드카드 → 접두사 검색
            prefix = q.replace('?', 'a')
            suffix = q.replace('?', 'z')
            word_list = word_dict[length]
        else:  # 접두사에 와일드카드 → 단어와 쿼리 모두 뒤집어서 접두사 검색
            q = q[::-1]
            prefix = q.replace('?', 'a')
            suffix = q.replace('?', 'z')
            word_list = reversed_dict[length]

        # 이진 탐색으로 범위 계산
        left = bisect.bisect_left(word_list, prefix)
        right = bisect.bisect_right(word_list, suffix)
        result.append(right - left)

    return result


'''
# 정확성 테스트 통과, 효율성 테스트 통과 x
# 효율성 테스트에선 O(N * M) 가까운 시간이 걸릴 수 있어서 시간 초과가 발생
from collections import defaultdict

def solution(words, queries):
    length_dict = defaultdict(list)

    # 전처리: 길이별로 단어 분류
    for word in words:
        length_dict[len(word)].append(word)

    result = []
    for query in queries:
        l = len(query)
        candidates = length_dict[l]

        # 접두사 패턴
        if query[0] != '?':
            prefix = query.split('?')[0]
            count = sum(word.startswith(prefix) for word in candidates)
        # 접미사 패턴
        else:
            suffix = query[query.rfind('?')+1:]
            count = sum(word.endswith(suffix) for word in candidates)

        result.append(count)

    return result
'''