'''
리스트의 길이가 길기 때문에 그래프를 완전탐색과 같은 형태로 순회하는 것은 어렵다. 따라서 각 그래프에 대하여 해당 그래프임을 판별할 수 있는 특정한 조건을 지닌 노드가 있는지를 확인해야 한다.
각각의 그래프는 다음과 같은 조건을 통해 구분할 수 있다.

- '생성된 정점'은 나가는 간선의 수가 2 이상이고, 들어오는 간선의 수가 0이다.
- '막대 모양 그래프'의 수는 나가는 간선의 수가 0, 들어오는 간선의 수가 1인 노드의 개수와 같다.
- '8자 모양 그래프'의 수는 나가는 간선의 수가 2, 들어오는 간선의 수도 2인 노드의 개수와 같다.
- '도넛 모양 그래프'는 '생성된 정점'의 나가는 간선의 수에서 막대 모양 그래프와 8자 모양 그래프의 개수를 빼서 구한다.

이때, 막대 모양 그래프와 8자 모양 그래프의 경우 '생성된 정점'에서 들어오는 간선이 존재하므로 각각 1 이상, 2 이상으로 조건을 설정한다.
이를 바탕으로 다음과 같이 동작하도록 코드를 작성한다.

1. edges의 요소를 순회하면서 각 노드별로 들어오는 간선과 나가는 간선의 개수를 표시한다.
2. 각 노드별 간선들의 수를 확인하여 상기의 조건에 맞는 노드의 개수를 answer에 추가한다.

레퍼런스 : https://velog.io/@mino0121/ProgrammersPython-%EB%8F%84%EB%84%9B%EA%B3%BC-%EB%A7%89%EB%8C%80%EA%B7%B8%EB%9E%98%ED%94%84
'''

def solution(edges):
    answers = [0, 0, 0, 0]
    n = 1000000
    maxV = 0
    edges_in, edges_out = [0]*n, [0]*n
    for i, j in edges:
        edges_in[i] += 1
        edges_out[j] += 1
        maxV = max(i, j, maxV)

    for i in range(1, maxV+1):
        if edges_in[i] >= 2 and edges_out[i] >= 2:
            answers[3] += 1
        if edges_out[i] > 0 and edges_in[i] == 0:
            answers[2] += 1
        if edges_out[i] == 0 and edges_in[i] >= 2:
            answers[0] = i

    answers[1] = edges_in[answers[0]] - (answers[2] + answers[3])
    
    return answers